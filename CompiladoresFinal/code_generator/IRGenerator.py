from typing import List, Dict, Any
from generated.ScriptLangVisitor import ScriptLangVisitor
from generated.ScriptLangParser import ScriptLangParser

class IRInstruction:
    def __init__(self, op: str, arg1=None, arg2=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

class IRGenerator(ScriptLangVisitor):
    def __init__(self):
        super().__init__()
        self.scenes: Dict[str, List[IRInstruction]] = {}
        self.current_scene = None
        self.first_scene = None
    
    def visitProgram(self, ctx: ScriptLangParser.ProgramContext):
        for scene_ctx in ctx.scene():
            self.visitScene(scene_ctx)
        return None
    
    def visitScene(self, ctx: ScriptLangParser.SceneContext):
        scene_name = ctx.ID().getText()
        self.current_scene = scene_name
        self.scenes[scene_name] = []
        if self.first_scene is None:
            self.first_scene = scene_name
        for dialogue_ctx in ctx.dialogue():
            self.visitDialogue(dialogue_ctx)
        return None
    
    def visitDialogue(self, ctx: ScriptLangParser.DialogueContext):
        if ctx.sayStmt():
            text = ctx.sayStmt().STRING().getText()[1:-1]
            self.scenes[self.current_scene].append(IRInstruction("PRINT", text))
        elif ctx.optionStmt():
            opt = ctx.optionStmt()
            text = opt.STRING().getText()[1:-1]
            target = opt.ID().getText()
            self.scenes[self.current_scene].append(IRInstruction("OPTION", text, target))
        return None
    
    def get_ir(self):
        return {"scenes": self.scenes, "first_scene": self.first_scene}
