# Generated from Expr.g4 by ANTLR 4.11.1
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
        4,1,9,19,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,2,1,2,1,2,0,0,3,0,2,4,0,2,1,0,2,3,1,0,4,6,16,0,6,1,
        0,0,0,2,14,1,0,0,0,4,16,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,
        0,0,9,10,7,0,0,0,10,11,3,2,1,0,11,12,7,1,0,0,12,15,1,0,0,0,13,15,
        5,8,0,0,14,9,1,0,0,0,14,13,1,0,0,0,15,3,1,0,0,0,16,17,5,1,0,0,17,
        5,1,0,0,0,1,14
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'list'", "'+'", "'-'", "'rent'", "'utilities'", 
                     "'grocery'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "OP_ADD", "OP_SUB", "CAT_RENT", 
                      "CAT_UTIL", "CAT_GROCERY", "NEWLINE", "COST", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_command = 2

    ruleNames =  [ "prog", "expr", "command" ]

    EOF = Token.EOF
    T__0=1
    OP_ADD=2
    OP_SUB=3
    CAT_RENT=4
    CAT_UTIL=5
    CAT_GROCERY=6
    NEWLINE=7
    COST=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr()
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token
            self.number = None # ExprContext
            self.cat = None # Token

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def OP_ADD(self):
            return self.getToken(ExprParser.OP_ADD, 0)

        def OP_SUB(self):
            return self.getToken(ExprParser.OP_SUB, 0)

        def CAT_RENT(self):
            return self.getToken(ExprParser.CAT_RENT, 0)

        def CAT_UTIL(self):
            return self.getToken(ExprParser.CAT_UTIL, 0)

        def CAT_GROCERY(self):
            return self.getToken(ExprParser.CAT_GROCERY, 0)

        def COST(self):
            return self.getToken(ExprParser.COST, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 10
                localctx.number = self.expr()
                self.state = 11
                localctx.cat = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                    localctx.cat = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(ExprParser.COST)
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


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ExprParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





