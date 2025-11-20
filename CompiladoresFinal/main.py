from antlr4 import FileStream, CommonTokenStream
from generated.ScriptLangLexer import ScriptLangLexer
from generated.ScriptLangParser import ScriptLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from code_generator.IRGenerator import IRGenerator
from code_generator.PythonCodeGenerator import PythonCodeGenerator
import sys
import os

def compile_file(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' no existe")
        return False
    
    print(f"\nCompilando: {input_file}")
    
    # Análisis léxico y sintáctico
    try:
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = ScriptLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = ScriptLangParser(tokens)
        tree = parser.program()
    except Exception as e:
        print(f"Error de sintaxis: {e}")
        return False
    
    # Análisis semántico
    semantic = SemanticVisitor()
    semantic.visitProgram(tree)
    
    if semantic.errors:
        print("\nErrores semánticos:")
        for error in semantic.errors:
            print(f"  {error}")
        return False
    
    print("✓ Sin errores semánticos")
    
    # Generación de IR
    ir_gen = IRGenerator()
    ir_gen.visitProgram(tree)
    ir = ir_gen.get_ir()
    
    # Generación de Python
    py_gen = PythonCodeGenerator()
    python_code = py_gen.generate(ir)
    
    # Guardar
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(python_code)
    
    print(f"✓ Generado: {output_file}\n")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <entrada.txt> [salida.py]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output.py"
        compile_file(input_file, output_file)
