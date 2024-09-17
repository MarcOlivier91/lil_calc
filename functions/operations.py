from termcolor import colored
import os
from time import sleep
from functions.inputs import *

def operations() :     
    operationChoice = input()
    os.system('cls')
    a = int(input(colored("Choose your first number : ", "white", "on_blue")))
    b = int(input(colored("Choose your second number : ", "white", "on_blue")))
    
    if operationChoice == 9:
        print("Bye")

    elif operationChoice == 1 :
        result = int(a) + int(b)
        print(f"The result is {result}")
    
    elif operationChoice == 2 :
        result = int(a) - int(b)
        print(f"The result is {result}")
    
    elif operationChoice == 3 :
        result = int(a) * int(b)
        print(f"The result is {result}")
        
    elif operationChoice == 4 :
        if int(a) or int(b) != 0 :                
            result = int(a) / int(b)
            print(f"The result is {result}")
        else:                
            print(colored("You cannot divide by zero !", "black", "on_red"))

