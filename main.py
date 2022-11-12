import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
 
 
def main(argv):
    calculation = input("Enter your expression: ")

    calc = InputStream(calculation)
    lexer = ExprLexer(calc)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
 
    res = MyExprVisitor().visitProg(tree)  # Evaluate the expression
 
    print(calculation, '=', res)
 
 
if __name__ == '__main__':
    main(sys.argv)


