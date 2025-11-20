from generated.ScriptLangVisitor import ScriptLangVisitor
from generated.ScriptLangParser import ScriptLangParser
from .SymbolTable import SymbolTable

class SemanticVisitor(ScriptLangVisitor):
    def __init__(self):
        super().__init__()
        self.table = SymbolTable()
        self.errors = []
        self.scene_references = []
    
    def error(self, ctx, message: str):
        line = getattr(ctx.start, "line", "?")
        self.errors.append(f"[Línea {line}] Error: {message}")
    
    def visitProgram(self, ctx: ScriptLangParser.ProgramContext):
        for scene_ctx in ctx.scene():
            scene_name = scene_ctx.ID().getText()
            if not self.table.add_scene(scene_name):
                self.error(scene_ctx, f"Escena '{scene_name}' duplicada")
        
        for scene_ctx in ctx.scene():
            self.visitScene(scene_ctx)
        
        for scene_name, line, ref_scene in self.scene_references:
            if not self.table.scene_exists(ref_scene):
                self.errors.append(f"[Línea {line}] Error: Escena '{ref_scene}' no existe")
        return None
    
    def visitScene(self, ctx: ScriptLangParser.SceneContext):
        scene_name = ctx.ID().getText()
        for dialogue_ctx in ctx.dialogue():
            if dialogue_ctx.optionStmt():
                option_ctx = dialogue_ctx.optionStmt()
                target = option_ctx.ID().getText()
                line = option_ctx.start.line
                self.scene_references.append((scene_name, line, target))
        return None
