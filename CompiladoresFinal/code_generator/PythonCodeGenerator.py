from typing import Dict, List, Any
from .IRGenerator import IRInstruction

class PythonCodeGenerator:
    def __init__(self):
        self.indent_level = 0
    
    def indent(self):
        self.indent_level += 1
    
    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1
    
    def get_indent(self):
        return "    " * self.indent_level
    
    def generate(self, ir: Dict[str, Any]) -> str:
        lines = ["# Guión interactivo generado", ""]
        scenes = ir.get("scenes", {})
        first_scene = ir.get("first_scene")
        
        for scene_name, instructions in scenes.items():
            lines.extend(self.generate_scene(scene_name, instructions))
            lines.append("")
        
        if first_scene:
            lines.append(f"if __name__ == '__main__':")
            lines.append(f"    {first_scene}()")
        
        return "\n".join(lines)
    
    def generate_scene(self, scene_name: str, instructions: List[IRInstruction]):
        lines = [f"def {scene_name}():"]
        self.indent()
        
        if not instructions:
            lines.append(self.get_indent() + "pass")
            self.dedent()
            return lines
        
        for inst in instructions:
            for line in self.generate_instruction(inst):
                lines.append(self.get_indent() + line)
        
        self.dedent()
        return lines
    
    def generate_instruction(self, inst: IRInstruction):
        if inst.op == "PRINT":
            return [f'print("{inst.arg1}")']
        elif inst.op == "OPTION":
            return [
                f'opcion = input("{inst.arg1} -> ")',
                f'if opcion.strip():',
                f'    {inst.arg2}()'
            ]
        return []
