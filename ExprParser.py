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
        4,1,18,41,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,17,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,1,0,1,2,2,
        0,2,0,4,1,0,9,11,1,0,12,13,1,0,5,6,1,0,3,4,47,0,4,1,0,0,0,2,16,1,
        0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,8,9,7,0,0,
        0,9,17,3,2,1,7,10,17,5,16,0,0,11,17,5,17,0,0,12,13,5,1,0,0,13,14,
        3,2,1,0,14,15,5,2,0,0,15,17,1,0,0,0,16,7,1,0,0,0,16,10,1,0,0,0,16,
        11,1,0,0,0,16,12,1,0,0,0,17,37,1,0,0,0,18,19,10,9,0,0,19,20,7,1,
        0,0,20,36,3,2,1,10,21,22,10,8,0,0,22,23,5,8,0,0,23,36,3,2,1,9,24,
        25,10,6,0,0,25,26,5,7,0,0,26,36,3,2,1,7,27,28,10,5,0,0,28,29,7,2,
        0,0,29,36,3,2,1,6,30,31,10,4,0,0,31,32,7,3,0,0,32,36,3,2,1,5,33,
        34,10,10,0,0,34,36,5,14,0,0,35,18,1,0,0,0,35,21,1,0,0,0,35,24,1,
        0,0,0,35,27,1,0,0,0,35,30,1,0,0,0,35,33,1,0,0,0,36,39,1,0,0,0,37,
        35,1,0,0,0,37,38,1,0,0,0,38,3,1,0,0,0,39,37,1,0,0,0,3,16,35,37
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'='", "'sin'", "'cos'", "'tan'", "'ADD'", "'SUB'", 
                     "'CHECK'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP_ADD", "OP_SUB", 
                      "OP_MUL", "OP_DIV", "OP_POW", "OP_EQ", "TRIG_SIN", 
                      "TRIG_COS", "TRIG_TAN", "FINANCE_ADD", "FINANCE_SUB", 
                      "FINANCE_CHECK", "NEWLINE", "NUM", "STR", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP_ADD=3
    OP_SUB=4
    OP_MUL=5
    OP_DIV=6
    OP_POW=7
    OP_EQ=8
    TRIG_SIN=9
    TRIG_COS=10
    TRIG_TAN=11
    FINANCE_ADD=12
    FINANCE_SUB=13
    FINANCE_CHECK=14
    NEWLINE=15
    NUM=16
    STR=17
    WS=18

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
            self.state = 4
            self.expr(0)
            self.state = 5
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


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(ExprParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrExpr" ):
                listener.enterStrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrExpr" ):
                listener.exitStrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrExpr" ):
                return visitor.visitStrExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OP_EQ(self):
            return self.getToken(ExprParser.OP_EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OP_POW(self):
            return self.getToken(ExprParser.OP_POW, 0)
        def OP_MUL(self):
            return self.getToken(ExprParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(ExprParser.OP_DIV, 0)
        def OP_ADD(self):
            return self.getToken(ExprParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(ExprParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class TrigExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.trig = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def TRIG_SIN(self):
            return self.getToken(ExprParser.TRIG_SIN, 0)
        def TRIG_COS(self):
            return self.getToken(ExprParser.TRIG_COS, 0)
        def TRIG_TAN(self):
            return self.getToken(ExprParser.TRIG_TAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigExpr" ):
                listener.enterTrigExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigExpr" ):
                listener.exitTrigExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigExpr" ):
                return visitor.visitTrigExpr(self)
            else:
                return visitor.visitChildren(self)


    class FinanceExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.finance = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def FINANCE_ADD(self):
            return self.getToken(ExprParser.FINANCE_ADD, 0)
        def FINANCE_SUB(self):
            return self.getToken(ExprParser.FINANCE_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinanceExpr" ):
                listener.enterFinanceExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinanceExpr" ):
                listener.exitFinanceExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinanceExpr" ):
                return visitor.visitFinanceExpr(self)
            else:
                return visitor.visitChildren(self)


    class FinancecheckExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.finance = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def FINANCE_CHECK(self):
            return self.getToken(ExprParser.FINANCE_CHECK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinancecheckExpr" ):
                listener.enterFinancecheckExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinancecheckExpr" ):
                listener.exitFinancecheckExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinancecheckExpr" ):
                return visitor.visitFinancecheckExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11]:
                localctx = ExprParser.TrigExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                localctx.trig = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                    localctx.trig = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 9
                localctx.right = self.expr(7)
                pass
            elif token in [16]:
                localctx = ExprParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(ExprParser.NUM)
                pass
            elif token in [17]:
                localctx = ExprParser.StrExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(ExprParser.STR)
                pass
            elif token in [1]:
                localctx = ExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(ExprParser.T__0)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(ExprParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.FinanceExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 19
                        localctx.finance = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.finance = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 20
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.EqExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 22
                        localctx.op = self.match(ExprParser.OP_EQ)
                        self.state = 23
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 25
                        localctx.op = self.match(ExprParser.OP_POW)
                        self.state = 26
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 28
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.FinancecheckExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 34
                        localctx.finance = self.match(ExprParser.FINANCE_CHECK)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         




