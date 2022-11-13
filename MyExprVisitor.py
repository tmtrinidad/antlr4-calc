from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
 
class MyExprVisitor(ExprVisitor):

    #rent_cost = 0.0
    #utilities_cost = 0.0
    #grocery_cost = 0.0
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
 
    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression
 
    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        self.visit(ctx.number)  # Evaluate expression and push to stack
 
        a = self.stack.pop()
        c = None

        if ctx.CAT_GROCERY:  
            if ctx.OP_ADD():
                c = 0 + a
            elif ctx.OP_SUB():
                c = 0 - a


        self.stack.append(c)
        print(f"grocery: {c}")
        return c
 
    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        c = int(str(ctx.INT()))  # Found a number, just insert to stack
        self.stack.append(c)
        return c
 
    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr

