# Generated from ScriptLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ScriptLangParser import ScriptLangParser
else:
    from ScriptLangParser import ScriptLangParser

# This class defines a complete generic visitor for a parse tree produced by ScriptLangParser.

class ScriptLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScriptLangParser#program.
    def visitProgram(self, ctx:ScriptLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLangParser#scene.
    def visitScene(self, ctx:ScriptLangParser.SceneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLangParser#dialogue.
    def visitDialogue(self, ctx:ScriptLangParser.DialogueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLangParser#sayStmt.
    def visitSayStmt(self, ctx:ScriptLangParser.SayStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLangParser#optionStmt.
    def visitOptionStmt(self, ctx:ScriptLangParser.OptionStmtContext):
        return self.visitChildren(ctx)



del ScriptLangParser