import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
 
 
def main(argv):
    print("Welcome to our budget tracker and calculator. If you would like to quit, please enter 'q'.")
    print("To open the budget tracker, enter 'b'")
    print("To open the  calculator, please enter 'c'\n")

    while True:
        user_input = input("Enter your command: \n")
        if user_input == 'q':
            print("Now quitting...")
            break
        elif user_input == 'c':
            print("To view previous calculation history, enter 'history'")
            print("To clear history, enter 'clear'")
            option = input("Please enter your command, or z to return to the menu: ")
            if option == 'z':
                continue
            elif option == 'clear':
                continue
            user_input = option
        elif user_input == 'b':
            print("\nWelcome to the budgeting application\n")
            print("Please enter a letter to add to your budget: ")
            print("   a: Rent/Housing Payments ")
            print("   b: Grocery")
            print("   c: Personal")
            print("   d: Other\n")
            user_input = input("Input: ")

        calc = InputStream(user_input)
        lexer = ExprLexer(calc)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
 
        res = MyExprVisitor().visitProg(tree)  # Evaluate the expression
        if (user_input != 'history') & (user_input != 'a'):
            print(user_input, '= ', res)
        else:
            print(res)
 
 
if __name__ == '__main__':
    main(sys.argv)
