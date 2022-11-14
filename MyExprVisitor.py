import math
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class MyExprVisitor(ExprVisitor):

    history = ["History: "]
    
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
 
    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression
 
    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        try:
            self.visit(ctx.left) # Evaluate the left expression and push to stack
        except:
            return 'ERROR'
            
        self.visit(ctx.right) # Evaluate the right expression and push to stack
        b = self.stack.pop() # b is the right side expression
        a = self.stack.pop()

        
        c = None


        if ctx.OP_ADD():
            c = a + b
            MyExprVisitor.history.append(f"{a} + {b} = {c}")
        elif ctx.OP_SUB():
            c = a - b
            MyExprVisitor.history.append(f"{a} - {b} = {c}")
        elif ctx.OP_MUL():
            c = a * b
            MyExprVisitor.history.append(f"{a} * {b} = {c}")
        elif ctx.OP_DIV():
            c = a / b
            MyExprVisitor.history.append(f"{a} / {b} = {c}")
        elif ctx.OP_POW():
            c = a ** b
            MyExprVisitor.history.append(f"{a} ^{b} = {c}")


        self.stack.append(c)

        return c
        #print(MyExprVisitor.history[1])
 
    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        c = float(str(ctx.NUM()))  # Found a number, just insert to stack
        self.stack.append(c)
        return c
 
    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr

    def visitStrExpr(self, ctx:ExprParser.StrExprContext):
        c = str(ctx.STR())  # Found a string, just insert to stack
        self.stack.append(c)
        if c == 'history':
            return MyExprVisitor.history
        elif c == 'clear':
            # clear the list
            c = "Calculations have been cleared."

        return c

    def visitTrigExpr(self, ctx:ExprParser.StrExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right) # Evaluate the right expression and push to stack
        b = self.stack.pop() # b is the right side expression
        a = self.stack.pop()

        c = None
        
        if a == 'tan':
            c = math.tan(b)
        if a == 'sin':
            c = math.sin(b)
        if a == 'cos':
            c = math.cos(b)
        else:
            c = "TRIG NOT FOUND"

        return c

    def clearHistory():
        MyExprVisitor.history.clear()
        MyExprVisitor.history.append("History: ")

