import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
 
 
def main(argv):
    print("Welcome to our calculator. If you would like to quit, please enter 'q'")

    while True:
        calculation = input("Enter your calculation: ")
        if calculation == 'q':
            print("Now quitting...")
            break

        calc = InputStream(calculation)
        lexer = ExprLexer(calc)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
 
        res = MyExprVisitor().visitProg(tree)  # Evaluate the expression
 
        print(calculation, '= ', res)
 
 
if __name__ == '__main__':
    main(sys.argv)


