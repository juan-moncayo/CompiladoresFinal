# Importaciones de ANTLR4 para el análisis
from antlr4 import FileStream, CommonTokenStream

# Clases generadas por ANTLR4 desde la gramática (.g4)
from generated.ScriptLangLexer import ScriptLangLexer
from generated.ScriptLangParser import ScriptLangParser

# Nuestros módulos del compilador
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from code_generator.IRGenerator import IRGenerator
from code_generator.PythonCodeGenerator import PythonCodeGenerator

import sys  # Para leer argumentos de consola
import os   # Para verificar archivos


def compile_file(input_file, output_file):
    """
    Función principal que ejecuta las 5 fases del compilador
    """
    
    # Verificar que el archivo de entrada existe
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' no existe")
        return False
    
    print(f"\nCompilando: {input_file}")
    
    # === FASE 1 y 2: Análisis léxico y sintáctico ===
    try:
        # Leer el archivo fuente
        input_stream = FileStream(input_file, encoding='utf-8')
        
        # LÉXICO: El lexer convierte el texto en tokens
        # Ej: "escena inicio" -> [TOKEN_ESCENA, TOKEN_ID]
        lexer = ScriptLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        
        # SINTÁCTICO: El parser verifica la estructura y crea el AST
        # Valida que siga las reglas de la gramática
        parser = ScriptLangParser(tokens)
        tree = parser.program()  # Árbol de sintaxis abstracta
        
    except Exception as e:
        print(f"Error de sintaxis: {e}")
        return False
    
    # === FASE 3: Análisis semántico ===
    # Verifica que el código tenga sentido:
    # - No haya escenas duplicadas
    # - Las referencias ir_a apunten a escenas que existen
    semantic = SemanticVisitor()
    semantic.visitProgram(tree)  # Recorre el AST validando
    
    # Si hay errores semánticos, los muestra y termina
    if semantic.errors:
        print("\nErrores semánticos:")
        for error in semantic.errors:
            print(f"  {error}")
        return False
    
    print("✓ Sin errores semánticos")
    
    # === FASE 4: Generar código intermedio (IR) ===
    # Convierte el AST en instrucciones simples como:
    # PRINT("texto") y OPTION("texto", destino)
    ir_gen = IRGenerator()
    ir_gen.visitProgram(tree)
    ir = ir_gen.get_ir()  # Obtiene la representación intermedia
    
    # === FASE 5: Generar código Python ===
    # Traduce las instrucciones IR a funciones Python
    # Cada escena se convierte en una función def
    py_gen = PythonCodeGenerator()
    python_code = py_gen.generate(ir)
    
    # Guardar el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(python_code)
    
    print(f"✓ Generado: {output_file}\n")
    return True


# Punto de entrada del programa
if __name__ == "__main__":
    # Verificar que se pasaron argumentos
    if len(sys.argv) < 2:
        print("Uso: python main.py <entrada.txt> [salida.py]")
    else:
        # Obtener archivo de entrada (obligatorio)
        input_file = sys.argv[1]
        # Archivo de salida (opcional, por defecto output.py)
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output.py"
        # Ejecutar el compilador
        compile_file(input_file, output_file)