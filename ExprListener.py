# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#strExpr.
    def enterStrExpr(self, ctx:ExprParser.StrExprContext):
        pass

    # Exit a parse tree produced by ExprParser#strExpr.
    def exitStrExpr(self, ctx:ExprParser.StrExprContext):
        pass


    # Enter a parse tree produced by ExprParser#eqExpr.
    def enterEqExpr(self, ctx:ExprParser.EqExprContext):
        pass

    # Exit a parse tree produced by ExprParser#eqExpr.
    def exitEqExpr(self, ctx:ExprParser.EqExprContext):
        pass


    # Enter a parse tree produced by ExprParser#infixExpr.
    def enterInfixExpr(self, ctx:ExprParser.InfixExprContext):
        pass

    # Exit a parse tree produced by ExprParser#infixExpr.
    def exitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        pass


    # Enter a parse tree produced by ExprParser#funcExpr.
    def enterFuncExpr(self, ctx:ExprParser.FuncExprContext):
        pass

    # Exit a parse tree produced by ExprParser#funcExpr.
    def exitFuncExpr(self, ctx:ExprParser.FuncExprContext):
        pass


    # Enter a parse tree produced by ExprParser#numberExpr.
    def enterNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExprParser#numberExpr.
    def exitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ExprParser#trigExpr.
    def enterTrigExpr(self, ctx:ExprParser.TrigExprContext):
        pass

    # Exit a parse tree produced by ExprParser#trigExpr.
    def exitTrigExpr(self, ctx:ExprParser.TrigExprContext):
        pass


    # Enter a parse tree produced by ExprParser#financeExpr.
    def enterFinanceExpr(self, ctx:ExprParser.FinanceExprContext):
        pass

    # Exit a parse tree produced by ExprParser#financeExpr.
    def exitFinanceExpr(self, ctx:ExprParser.FinanceExprContext):
        pass


    # Enter a parse tree produced by ExprParser#financecheckExpr.
    def enterFinancecheckExpr(self, ctx:ExprParser.FinancecheckExprContext):
        pass

    # Exit a parse tree produced by ExprParser#financecheckExpr.
    def exitFinancecheckExpr(self, ctx:ExprParser.FinancecheckExprContext):
        pass


    # Enter a parse tree produced by ExprParser#parensExpr.
    def enterParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ExprParser#parensExpr.
    def exitParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass



del ExprParser