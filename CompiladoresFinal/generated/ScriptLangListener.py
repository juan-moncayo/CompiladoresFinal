# Generated from ScriptLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ScriptLangParser import ScriptLangParser
else:
    from ScriptLangParser import ScriptLangParser

# This class defines a complete listener for a parse tree produced by ScriptLangParser.
class ScriptLangListener(ParseTreeListener):

    # Enter a parse tree produced by ScriptLangParser#program.
    def enterProgram(self, ctx:ScriptLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by ScriptLangParser#program.
    def exitProgram(self, ctx:ScriptLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by ScriptLangParser#scene.
    def enterScene(self, ctx:ScriptLangParser.SceneContext):
        pass

    # Exit a parse tree produced by ScriptLangParser#scene.
    def exitScene(self, ctx:ScriptLangParser.SceneContext):
        pass


    # Enter a parse tree produced by ScriptLangParser#dialogue.
    def enterDialogue(self, ctx:ScriptLangParser.DialogueContext):
        pass

    # Exit a parse tree produced by ScriptLangParser#dialogue.
    def exitDialogue(self, ctx:ScriptLangParser.DialogueContext):
        pass


    # Enter a parse tree produced by ScriptLangParser#sayStmt.
    def enterSayStmt(self, ctx:ScriptLangParser.SayStmtContext):
        pass

    # Exit a parse tree produced by ScriptLangParser#sayStmt.
    def exitSayStmt(self, ctx:ScriptLangParser.SayStmtContext):
        pass


    # Enter a parse tree produced by ScriptLangParser#optionStmt.
    def enterOptionStmt(self, ctx:ScriptLangParser.OptionStmtContext):
        pass

    # Exit a parse tree produced by ScriptLangParser#optionStmt.
    def exitOptionStmt(self, ctx:ScriptLangParser.OptionStmtContext):
        pass



del ScriptLangParser