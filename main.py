import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
 
 
def main(argv):
    print("Welcome to our calculator. If you would like to quit, please enter 'q'.")
    print("To view other commands, enter 'c'\n")

    while True:
        calculation = input("Enter your calculation: \n")
        if calculation == 'q':
            print("Now quitting...")
            break
        elif calculation == 'c':
            print("To view previous calculation history, enter 'history'")
            print("To clear history, enter 'clear'")
            option = input("Please enter your command, or z to return to the menu: ")
            if option == 'z':
                continue
            elif option == 'clear':
                continue
            calculation = option
            

        calc = InputStream(calculation)
        lexer = ExprLexer(calc)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
 
        res = MyExprVisitor().visitProg(tree)  # Evaluate the expression
        if calculation != 'history':
            print(calculation, '= ', res)
        else:
            print(res)
 
 
if __name__ == '__main__':
    main(sys.argv)
