import math
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class MyExprVisitor(ExprVisitor):

    history = ["History: "]
    variables = {}
    finances = {}

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
            return 'There is an error with the expression'
            
        try:
            self.visit(ctx.right) # Evaluate the right expression and push to stack
        except:
            return 'There is an error with the expression'
        
        b = self.stack.pop() # b is the right side expression
        a = self.stack.pop()
        
        if type(b) is str:
            if MyExprVisitor.variableExists(b):
                b = MyExprVisitor.variables.get(b)
            else:
                return f"The variable '{b}' has not yet been defined"
        
        if type(a) is str:
            if MyExprVisitor.variableExists(a):
                a = MyExprVisitor.variables.get(a)
            else:
                return f"The variable '{a}' has not yet been defined"
            
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
        try:
            c = float(str(ctx.NUM()))  # Found a number, just insert to stack
            self.stack.append(c)
        except:
            return "\nYour number contains an unidentified character.\n" \
                   "Please make sure you have spaces between numbers and operators\n" \
                   "    EX: 5 + 5\n"
        return c
 
    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr

    def visitStrExpr(self, ctx:ExprParser.StrExprContext):
        c = str(ctx.STR())  # Found a string, just insert to stack
        self.stack.append(c)
        if c == 'history':
            return MyExprVisitor.loopHistoryList()
        elif c == 'clear':
            # clear the list
            MyExprVisitor.clear_history()
            c = "\nCalculations have been cleared.\n"
        else:
            c = "\nYou have entered a command which is not known. \n"
        return c

    def visitTrigExpr(self, ctx:ExprParser.StrExprContext):
        self.visit(ctx.right) # Evaluate the right expression and push to stack
        b = self.stack.pop()  # b is the right side expression

        if type(b) is str:
            if MyExprVisitor.variableExists(b):
                b = MyExprVisitor.variables.get(b)
            else:
                return f"The variable '{b}' has not yet been defined"

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

        return c

    def visitEqExpr(self, ctx:ExprParser.EqExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)
        b = self.stack.pop() # b is the right side expression
        a = self.stack.pop()

        MyExprVisitor.addVariable(a,b)
        MyExprVisitor.history.append(f"{a} = {b}")

        return "\nVariable has been added\n"

    def visitFuncExpr(self, ctx:ExprParser.EqExprContext):
        self.visit(ctx.right) # Evaluate the right expression and push to stack
        b = self.stack.pop()  # b is the right side expression

        if type(b) is str:
            if MyExprVisitor.variableExists(b):
                b = MyExprVisitor.variables.get(b)
            else:
                return f"The variable '{b}' has not yet been defined"

        c = 0

        if ctx.FUNC_E():
            c = math.e * b
            MyExprVisitor.history.append(f"e {b} = {c}")
        elif ctx.FUNC_LN():
            c = math.log(b)
            MyExprVisitor.history.append(f"ln {b} = {c}")
        elif ctx.FUNC_LOG():
            c = math.log10(b)
            MyExprVisitor.history.append(f"log {b} = {c}")

        return c

    def visitFinanceExpr(self, ctx:ExprParser.FinanceExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)
        b = self.stack.pop()  # b is the number value
        a = self.stack.pop()  # a is the category

        if type(a) is not str:
            return "\nPlease use a string for your category name\n"
        if not MyExprVisitor.financeExists(a):
            MyExprVisitor.addFinance(a, b)
            s = MyExprVisitor.loopFinanceDictionary()
            return s

        if ctx.FINANCE_ADD():
            b = MyExprVisitor.finances.get(a) + b
            MyExprVisitor.finances.update({a: b})
            s = MyExprVisitor.loopFinanceDictionary()
            return s
        elif ctx.FINANCE_SUB():
            b = MyExprVisitor.finances.get(a) - b
            MyExprVisitor.finances.update({a: b})
            s = MyExprVisitor.loopFinanceDictionary()
            return s

    def visitFinanceCheckExpr(self, ctx:ExprParser.FinancecheckExprContext):
        """
        Checks the budget for the specified category
        :param ctx:
        :return: The value in the finance budget for that category
        """
        self.visit(ctx.left)
        a = self.stack.pop()

        return f"${MyExprVisitor.variables.get(a)}"

    @staticmethod
    def variableExists(var):
        """
        Return True if variable exists in the dictionary
        Returns False if it does not
        """
        x = MyExprVisitor.variables.get(var)
        if x is None:
            return False
        return True

    @staticmethod
    def loopFinanceDictionary():
        statement = "\nBUDGET:  \n"
        
        for x, y in MyExprVisitor.finances.items():
            statement += f"   {x}: ${y}\n"
            
        return statement

    @staticmethod
    def loopHistoryList():
        statement = ""

        for x in MyExprVisitor.history:
            statement += f"  {x}\n"

        return statement
    
    @staticmethod
    def addVariable(var, value):
        """
        Add variable to the dictionary
        """
        MyExprVisitor.variables[var] = value

    @staticmethod
    def addFinance(var, value):
        """
        Add variable to the dictionary
        """
        MyExprVisitor.finances[var] = value

    @staticmethod
    def financeExists(var):
        """
        Return True if variable exists in the dictionary
        Returns False if it does not
        """
        x = MyExprVisitor.finances.get(var)
        if x is None:
            return False
        return True

    @staticmethod
    def clear_history():
        MyExprVisitor.history.clear()
        MyExprVisitor.history.append("History: ")

