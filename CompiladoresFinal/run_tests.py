#!/usr/bin/env python3
"""
Script de automatización de pruebas para el compilador ScriptLang
Ejecuta todos los casos de prueba válidos e inválidos automáticamente
"""
import os
import sys
import subprocess  # Para ejecutar comandos de consola
from pathlib import Path  # Para manejar rutas de archivos


# Clase para dar colores a la salida en consola
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    """Imprime un encabezado bonito con líneas"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(70)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}\n")


def print_test(name, status, message=""):
    """Imprime el resultado de un test con ✓ o ✗"""
    status_symbol = f"{Colors.GREEN}✓{Colors.RESET}" if status else f"{Colors.RED}✗{Colors.RESET}"
    print(f"{status_symbol} {name}: {message}")


def run_compiler(input_file, output_file):
    """Ejecuta el compilador main.py y retorna si fue exitoso"""
    try:
        # Ejecuta: python main.py entrada.txt salida.py
        result = subprocess.run(
            ['python', 'main.py', input_file, output_file],
            capture_output=True,
            text=True,
            timeout=10  # Máximo 10 segundos
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout"
    except Exception as e:
        return False, "", str(e)


def run_generated_script(script_file):
    """Ejecuta el script Python generado para verificar que funciona"""
    try:
        result = subprocess.run(
            ['python', script_file],
            capture_output=True,
            text=True,
            timeout=5,
            input="\n" * 10  # Simula 10 enters para las opciones
        )
        return True, result.stdout
    except subprocess.TimeoutExpired:
        return False, "Timeout en ejecución"
    except Exception as e:
        return False, str(e)


def run_valid_tests():
    """Ejecuta todos los tests que deben compilar correctamente"""
    print_header("PRUEBAS VÁLIDAS (Deben compilar y ejecutar)")
    
    tests_dir = Path('tests')
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)  # Crea carpeta output si no existe
    
    # Busca todos los archivos test*.txt
    valid_tests = sorted([f for f in tests_dir.glob('test*.txt')])
    
    passed = 0
    failed = 0
    
    for test_file in valid_tests:
        test_name = test_file.stem  # Nombre sin extensión
        output_file = output_dir / f"{test_name}.py"
        
        # Intenta compilar el archivo
        success, stdout, stderr = run_compiler(str(test_file), str(output_file))
        
        if success:
            # Si compiló, intenta ejecutar el script generado
            exec_success, exec_output = run_generated_script(str(output_file))
            if exec_success:
                print_test(test_name, True, "Compilado y ejecutado correctamente")
                passed += 1
            else:
                print_test(test_name, False, f"Error en ejecución: {exec_output[:50]}")
                failed += 1
        else:
            print_test(test_name, False, "Error de compilación")
            if stderr:
                print(f"  {Colors.YELLOW}└─ {stderr[:100]}{Colors.RESET}")
            failed += 1
    
    print(f"\n{Colors.BOLD}Resultado: {Colors.GREEN}{passed} exitosos{Colors.RESET}, "
          f"{Colors.RED}{failed} fallidos{Colors.RESET}")
    return passed, failed


def run_error_tests():
    """Ejecuta tests que DEBEN fallar (tienen errores a propósito)"""
    print_header("PRUEBAS CON ERRORES (Deben detectar errores)")
    
    tests_dir = Path('tests')
    
    # Busca todos los archivos error*.txt
    error_tests = sorted([f for f in tests_dir.glob('error*.txt')])
    
    passed = 0
    failed = 0
    
    for test_file in error_tests:
        test_name = test_file.stem
        output_file = Path('output') / f"{test_name}_should_fail.py"
        
        # Compila (esperamos que falle)
        success, stdout, stderr = run_compiler(str(test_file), str(output_file))
        
        if not success:
            # Bien! El compilador detectó el error
            # Determinamos qué tipo de error fue
            error_type = "desconocido"
            if "semántico" in stdout.lower() or "no existe" in stdout.lower() or "duplicada" in stdout.lower():
                error_type = "semántico"
            elif "sintaxis" in stdout.lower() or "syntax" in stdout.lower():
                error_type = "sintáctico"
            else:
                error_type = "léxico/sintáctico"
            
            print_test(test_name, True, f"Error {error_type} detectado correctamente")
            # Muestra las líneas de error
            if stdout:
                error_lines = [line for line in stdout.split('\n') if 'Error' in line]
                for line in error_lines[:2]:
                    print(f"  {Colors.YELLOW}└─ {line.strip()}{Colors.RESET}")
            passed += 1
        else:
            # Mal! Debió fallar pero no falló
            print_test(test_name, False, "No detectó el error esperado")
            failed += 1
    
    print(f"\n{Colors.BOLD}Resultado: {Colors.GREEN}{passed} errores detectados{Colors.RESET}, "
          f"{Colors.RED}{failed} no detectados{Colors.RESET}")
    return passed, failed


def generate_test_report():
    """Genera un reporte en Markdown con los resultados"""
    report_file = Path('REPORTE_PRUEBAS.md')
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Reporte de Pruebas - Compilador ScriptLang\n\n")
        f.write("## Resumen de Ejecución\n\n")
        
        # Tabla de tests válidos
        f.write("### Pruebas Válidas\n\n")
        f.write("| Test | Descripción | Estado |\n")
        f.write("|------|-------------|--------|\n")
        
        tests_dir = Path('tests')
        for test_file in sorted(tests_dir.glob('test*.txt')):
            content = test_file.read_text(encoding='utf-8')
            desc = content.split('\n')[0][:50]  # Primera línea como descripción
            output_file = Path('output') / f"{test_file.stem}.py"
            
            success, _, _ = run_compiler(str(test_file), str(output_file))
            status = "✅ Pasó" if success else "❌ Falló"
            
            f.write(f"| {test_file.stem} | {desc} | {status} |\n")
        
        # Tabla de tests con errores
        f.write("\n### Pruebas con Errores Esperados\n\n")
        f.write("| Test | Tipo de Error | Estado |\n")
        f.write("|------|---------------|--------|\n")
        
        for test_file in sorted(tests_dir.glob('error*.txt')):
            output_file = Path('output') / f"{test_file.stem}_fail.py"
            success, stdout, _ = run_compiler(str(test_file), str(output_file))
            
            error_type = "Semántico" if "semántico" in stdout.lower() else "Sintáctico/Léxico"
            status = "✅ Detectado" if not success else "❌ No detectado"
            
            f.write(f"| {test_file.stem} | {error_type} | {status} |\n")
        
        f.write(f"\n---\n*Generado automáticamente por run_tests.py*\n")
    
    print(f"\n{Colors.GREEN}Reporte generado: {report_file}{Colors.RESET}")


def main():
    """Función principal que ejecuta todas las pruebas"""
    print_header("SISTEMA DE PRUEBAS AUTOMATIZADO - COMPILADOR SCRIPTLANG")
    
    # Verificar que existen los archivos necesarios
    if not Path('main.py').exists():
        print(f"{Colors.RED}Error: main.py no encontrado{Colors.RESET}")
        sys.exit(1)
    
    if not Path('tests').exists():
        print(f"{Colors.RED}Error: carpeta tests/ no encontrada{Colors.RESET}")
        sys.exit(1)
    
    # Ejecutar las dos categorías de pruebas
    valid_passed, valid_failed = run_valid_tests()
    error_passed, error_failed = run_error_tests()
    
    # Mostrar resumen final
    print_header("RESUMEN FINAL")
    total_passed = valid_passed + error_passed
    total_failed = valid_failed + error_failed
    total = total_passed + total_failed
    
    print(f"Total de pruebas: {total}")
    print(f"{Colors.GREEN}Exitosas: {total_passed}{Colors.RESET}")
    print(f"{Colors.RED}Fallidas: {total_failed}{Colors.RESET}")
    print(f"Porcentaje de éxito: {(total_passed/total*100):.1f}%\n")
    
    # Generar el reporte markdown
    generate_test_report()
    
    return 0 if total_failed == 0 else 1


# Punto de entrada
if __name__ == "__main__":
    sys.exit(main())