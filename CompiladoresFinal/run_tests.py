#!/usr/bin/env python3
"""
Script de automatización de pruebas para el compilador ScriptLang
Ejecuta todos los casos de prueba válidos e inválidos automáticamente
"""
import os
import sys
import subprocess
from pathlib import Path

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(70)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.RESET}\n")

def print_test(name, status, message=""):
    status_symbol = f"{Colors.GREEN}✓{Colors.RESET}" if status else f"{Colors.RED}✗{Colors.RESET}"
    print(f"{status_symbol} {name}: {message}")

def run_compiler(input_file, output_file):
    """Ejecuta el compilador y retorna True si fue exitoso"""
    try:
        result = subprocess.run(
            ['python', 'main.py', input_file, output_file],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout"
    except Exception as e:
        return False, "", str(e)

def run_generated_script(script_file):
    """Ejecuta el script generado y retorna True si no hay errores"""
    try:
        result = subprocess.run(
            ['python', script_file],
            capture_output=True,
            text=True,
            timeout=5,
            input="\n" * 10  # Simula enters para las opciones
        )
        return True, result.stdout
    except subprocess.TimeoutExpired:
        return False, "Timeout en ejecución"
    except Exception as e:
        return False, str(e)

def run_valid_tests():
    """Ejecuta todos los tests válidos"""
    print_header("PRUEBAS VÁLIDAS (Deben compilar y ejecutar)")
    
    tests_dir = Path('tests')
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    
    valid_tests = sorted([f for f in tests_dir.glob('test*.txt')])
    
    passed = 0
    failed = 0
    
    for test_file in valid_tests:
        test_name = test_file.stem
        output_file = output_dir / f"{test_name}.py"
        
        # Compilar
        success, stdout, stderr = run_compiler(str(test_file), str(output_file))
        
        if success:
            # Intentar ejecutar
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
    """Ejecuta todos los tests con errores esperados"""
    print_header("PRUEBAS CON ERRORES (Deben detectar errores)")
    
    tests_dir = Path('tests')
    
    error_tests = sorted([f for f in tests_dir.glob('error*.txt')])
    
    passed = 0
    failed = 0
    
    for test_file in error_tests:
        test_name = test_file.stem
        output_file = Path('output') / f"{test_name}_should_fail.py"
        
        # Compilar (debe fallar)
        success, stdout, stderr = run_compiler(str(test_file), str(output_file))
        
        if not success:
            # Determinar tipo de error
            error_type = "desconocido"
            if "semántico" in stdout.lower() or "no existe" in stdout.lower() or "duplicada" in stdout.lower():
                error_type = "semántico"
            elif "sintaxis" in stdout.lower() or "syntax" in stdout.lower():
                error_type = "sintáctico"
            else:
                error_type = "léxico/sintáctico"
            
            print_test(test_name, True, f"Error {error_type} detectado correctamente")
            if stdout:
                error_lines = [line for line in stdout.split('\n') if 'Error' in line]
                for line in error_lines[:2]:  # Mostrar primeras 2 líneas de error
                    print(f"  {Colors.YELLOW}└─ {line.strip()}{Colors.RESET}")
            passed += 1
        else:
            print_test(test_name, False, "No detectó el error esperado")
            failed += 1
    
    print(f"\n{Colors.BOLD}Resultado: {Colors.GREEN}{passed} errores detectados{Colors.RESET}, "
          f"{Colors.RED}{failed} no detectados{Colors.RESET}")
    return passed, failed

def generate_test_report():
    """Genera un reporte de pruebas en formato Markdown"""
    report_file = Path('REPORTE_PRUEBAS.md')
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Reporte de Pruebas - Compilador ScriptLang\n\n")
        f.write("## Resumen de Ejecución\n\n")
        
        # Tests válidos
        f.write("### Pruebas Válidas\n\n")
        f.write("| Test | Descripción | Estado |\n")
        f.write("|------|-------------|--------|\n")
        
        tests_dir = Path('tests')
        for test_file in sorted(tests_dir.glob('test*.txt')):
            content = test_file.read_text(encoding='utf-8')
            desc = content.split('\n')[0][:50]
            output_file = Path('output') / f"{test_file.stem}.py"
            
            success, _, _ = run_compiler(str(test_file), str(output_file))
            status = "✅ Pasó" if success else "❌ Falló"
            
            f.write(f"| {test_file.stem} | {desc} | {status} |\n")
        
        # Tests con errores
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
    print_header("SISTEMA DE PRUEBAS AUTOMATIZADO - COMPILADOR SCRIPTLANG")
    
    # Verificar estructura
    if not Path('main.py').exists():
        print(f"{Colors.RED}Error: main.py no encontrado{Colors.RESET}")
        sys.exit(1)
    
    if not Path('tests').exists():
        print(f"{Colors.RED}Error: carpeta tests/ no encontrada{Colors.RESET}")
        sys.exit(1)
    
    # Ejecutar pruebas válidas
    valid_passed, valid_failed = run_valid_tests()
    
    # Ejecutar pruebas de error
    error_passed, error_failed = run_error_tests()
    
    # Resumen final
    print_header("RESUMEN FINAL")
    total_passed = valid_passed + error_passed
    total_failed = valid_failed + error_failed
    total = total_passed + total_failed
    
    print(f"Total de pruebas: {total}")
    print(f"{Colors.GREEN}Exitosas: {total_passed}{Colors.RESET}")
    print(f"{Colors.RED}Fallidas: {total_failed}{Colors.RESET}")
    print(f"Porcentaje de éxito: {(total_passed/total*100):.1f}%\n")
    
    # Generar reporte
    generate_test_report()
    
    return 0 if total_failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())