import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
 
 
def main(argv):
    print("Welcome to our budget tracker and calculator. If you would like to quit, please enter 'q'.")
    print("To open the budget tracker, enter 'b'")
    print("To open the  calculator, please enter 'c'")
    print("To return to this menu, please enter 'z'\n")

    while True:
        user_input = input("Enter your command: \n")
        if (user_input == 'q'):
            print("\nNow quitting...")
            break
        elif user_input == 'c':
            print("\nWelcome to the Calculator application.")
            print("To view previous calculation history, enter 'history'")
            print("To clear history, enter 'clear'")
            print("To return to the menu, enter 'z'")
            continue
        elif user_input == 'b':
            print("\nWelcome to the budgeting application\n")
            print("To return to the menu, please enter 'z'\n")
            print("Please enter the name of the category to add to your budget,"
                  "\nthe operation you would like to perform: ADD or SUB"
                  "\nand the amount you would like to add: ")
            print("   EX: Rent ADD 1500")
            print("   EX: Grocery ADD 60")
            print("   EX: Rent SUB 100")
            print("_________________________________________\n")
            continue
        elif(user_input == 'z'):
            print("\nWelcome to our budget tracker and calculator. If you would like to quit, please enter 'q'.")
            print("To open the budget tracker, enter 'b'")
            print("To open the  calculator, please enter 'c'")
            print("To return to the menu, please enter 'z'\n")
            continue

        calc = InputStream(user_input)
        lexer = ExprLexer(calc)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
 
        res = MyExprVisitor().visitProg(tree)  # Evaluate the expression
        print(res)
 
 
if __name__ == '__main__':
    main(sys.argv)
