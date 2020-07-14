import math
import os  # We import os for access to system shells and commands. In this case 'echo' and 'clip'

def get_input():
    x = float(input("Enter a number: "))
    y = float(input("Enter a number: "))
    return x, y

def addition():
    x, y = get_input()
    return x + y

def subtraction():
    x, y = get_input()
    return x - y

def multiplication():
    x, y = get_input()
    return x*y

def division():
    x,y = get_input()
    return x / y

def square_root():
    x = float(input("Enter a number: "))
    return math.sqrt(x)
    
def menu():
    choice = 0
    print('-' * 35)
    print("Python Calculator\n1.) Addition\n2.) Subtraction\n" \
    "3.) Multiplication\n4.) Division\n5.) Square Root\n6.) Quit")

    while choice < 1 or choice > 6:

        try:
            choice = int(input(">> "))
        except ValueError:
            print("Please Enter a number that in the range of 1-6.")
            
    print('-' * 35)
    return choice

def sendToClipBoard(string):
    # the 'clip' command that the string is piped through
    # only works properly inside an Windows environment.
    os.system('echo ' + string +'| clip')

def main():
    result = None
    while True:
        user_input = menu()

        try:
            if user_input == 1:
                result = addition()
                
            elif user_input == 2:
                result = subtraction()
                
            elif user_input == 3:
                result = multiplication()
                
            elif user_input == 4:
                result = division()
            
            elif user_input == 5:
                result = square_root()
 
            elif user_input == 6:
                break
            
            print("Result: ", str(result))
            sendToClipBoard(str(result))
            
        except ValueError:
            print("Non Numerical data entry.")
        except ZeroDivisionError:
            print("Cannot Divide by Zero.")

    return result

main()
