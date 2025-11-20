# Generated from ScriptLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,4,1,22,8,1,11,1,12,1,23,1,1,
        1,1,1,2,1,2,3,2,30,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,0,0,5,0,2,4,6,8,0,0,39,0,11,1,0,0,0,2,17,1,0,0,0,4,29,1,0,0,0,
        6,31,1,0,0,0,8,35,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,
        0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,
        1,0,0,0,17,18,5,1,0,0,18,19,5,8,0,0,19,21,5,2,0,0,20,22,3,4,2,0,
        21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,
        0,0,0,25,26,5,3,0,0,26,3,1,0,0,0,27,30,3,6,3,0,28,30,3,8,4,0,29,
        27,1,0,0,0,29,28,1,0,0,0,30,5,1,0,0,0,31,32,5,4,0,0,32,33,5,9,0,
        0,33,34,5,5,0,0,34,7,1,0,0,0,35,36,5,6,0,0,36,37,5,9,0,0,37,38,5,
        7,0,0,38,39,5,8,0,0,39,40,5,5,0,0,40,9,1,0,0,0,3,13,23,29
    ]

class ScriptLangParser ( Parser ):

    grammarFileName = "ScriptLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'escena'", "'{'", "'}'", "'decir'", "';'", 
                     "'opcion'", "'ir_a'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "STRING", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_scene = 1
    RULE_dialogue = 2
    RULE_sayStmt = 3
    RULE_optionStmt = 4

    ruleNames =  [ "program", "scene", "dialogue", "sayStmt", "optionStmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    STRING=9
    WS=10
    LINE_COMMENT=11
    BLOCK_COMMENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ScriptLangParser.EOF, 0)

        def scene(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScriptLangParser.SceneContext)
            else:
                return self.getTypedRuleContext(ScriptLangParser.SceneContext,i)


        def getRuleIndex(self):
            return ScriptLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ScriptLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.scene()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 15
            self.match(ScriptLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SceneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ScriptLangParser.ID, 0)

        def dialogue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScriptLangParser.DialogueContext)
            else:
                return self.getTypedRuleContext(ScriptLangParser.DialogueContext,i)


        def getRuleIndex(self):
            return ScriptLangParser.RULE_scene

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScene" ):
                listener.enterScene(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScene" ):
                listener.exitScene(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScene" ):
                return visitor.visitScene(self)
            else:
                return visitor.visitChildren(self)




    def scene(self):

        localctx = ScriptLangParser.SceneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scene)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(ScriptLangParser.T__0)
            self.state = 18
            self.match(ScriptLangParser.ID)
            self.state = 19
            self.match(ScriptLangParser.T__1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.dialogue()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==6):
                    break

            self.state = 25
            self.match(ScriptLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DialogueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sayStmt(self):
            return self.getTypedRuleContext(ScriptLangParser.SayStmtContext,0)


        def optionStmt(self):
            return self.getTypedRuleContext(ScriptLangParser.OptionStmtContext,0)


        def getRuleIndex(self):
            return ScriptLangParser.RULE_dialogue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDialogue" ):
                listener.enterDialogue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDialogue" ):
                listener.exitDialogue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDialogue" ):
                return visitor.visitDialogue(self)
            else:
                return visitor.visitChildren(self)




    def dialogue(self):

        localctx = ScriptLangParser.DialogueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dialogue)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.sayStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.optionStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SayStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ScriptLangParser.STRING, 0)

        def getRuleIndex(self):
            return ScriptLangParser.RULE_sayStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSayStmt" ):
                listener.enterSayStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSayStmt" ):
                listener.exitSayStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSayStmt" ):
                return visitor.visitSayStmt(self)
            else:
                return visitor.visitChildren(self)




    def sayStmt(self):

        localctx = ScriptLangParser.SayStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sayStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ScriptLangParser.T__3)
            self.state = 32
            self.match(ScriptLangParser.STRING)
            self.state = 33
            self.match(ScriptLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ScriptLangParser.STRING, 0)

        def ID(self):
            return self.getToken(ScriptLangParser.ID, 0)

        def getRuleIndex(self):
            return ScriptLangParser.RULE_optionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionStmt" ):
                listener.enterOptionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionStmt" ):
                listener.exitOptionStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionStmt" ):
                return visitor.visitOptionStmt(self)
            else:
                return visitor.visitChildren(self)




    def optionStmt(self):

        localctx = ScriptLangParser.OptionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ScriptLangParser.T__5)
            self.state = 36
            self.match(ScriptLangParser.STRING)
            self.state = 37
            self.match(ScriptLangParser.T__6)
            self.state = 38
            self.match(ScriptLangParser.ID)
            self.state = 39
            self.match(ScriptLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





