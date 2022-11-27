import math
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class MyExprVisitor(ExprVisitor):

    history = ["History: "]
    rent = 0.0
    grocery = 0.0
    personal = 0.0
    other = 0.0
    variables = {}
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
        
        if MyExprVisitor.variableExists(b):
            b = MyExprVisitor.variables.get(b)

        if MyExprVisitor.variableExists(a):
            a = MyExprVisitor.variables.get(a)
            
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
            MyExprVisitor.clear_history()
            c = "Calculations have been cleared."
        return c

    def visitTrigExpr(self, ctx:ExprParser.StrExprContext):
        self.visit(ctx.right) # Evaluate the right expression and push to stack
        b = self.stack.pop()  # b is the right side expression

        if MyExprVisitor.variableExists(b):
            b = MyExprVisitor.variables.get(b)

        c = None
        
        if ctx.TRIG_TAN():
            c = math.tan(b)
            MyExprVisitor.history.append(f"tan {b} = {c}")
        elif ctx.TRIG_SIN():
            c = math.sin(b)
            MyExprVisitor.history.append(f"sin {b} = {c}")
        elif ctx.TRIG_COS():
            c = math.cos(b)
            MyExprVisitor.history.append(f"cos {b} = {c}")
        else:
            c = "TRIG NOT FOUND"

        return c

    def visitEqExpr(self, ctx:ExprParser.EqExprContext):
        self.visit(ctx.right)
        b = self.stack.pop() # b is the right side expression
        a = self.stack.pop()

        MyExprVisitor.addVariable(a,b)

        return "\nVariable has been added\n"

    def visitFinanceExpr(self, ctx:ExprParser.FinanceExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)
        b = self.stack.pop() # b is the number value
        a = self.stack.pop()
        c = 0

        if ctx.FINANCE_ADD():
            return 2
        elif ctx.FINANCE_SUB():
            return 3

    def visitFinanceCheckExpr(self, ctx:ExprParser.FinancecheckExprContext):
        self.visit(ctx.left)
        a = self.stack.pop()

        return f"${MyExprVisitor.variables.get(a)}"

    def variableExists(var):
        """
        Return True if variable exists in the dictionary
        Returns False if it does not
        """
        x = MyExprVisitor.variables.get(var)
        if x == None:
            return False
        return True

    def addVariable(var, value):
        """
        Add or changes the variable in the dictionary 
        """
        MyExprVisitor.variables[var] = value

    def clear_history():
        MyExprVisitor.history.clear()
        MyExprVisitor.history.append("History: ")

