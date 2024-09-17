from termcolor import colored
import os
from time import sleep
from functions.inputs import *

def operations() :     
    operationChoice = int(input())
    a = int(input(colored("Choose your first number : ", "white", "on_blue")))
    b = int(input(colored("Choose your second number : ", "white", "on_blue")))
    
    match operationChoice:
        case 9:
            print("Bye")

        case 1:
            result = int(a) + int(b)
            print(f"The result is {result}")
    
        case 2 :
            result = int(a) - int(b)
            print(f"The result is {result}")
    
        case 3 :
            result = int(a) * int(b)
            print(f"The result is {result}")
        
        case 4 :
            if int(a) != 0 and int(b) != 0 :                
                result = int(a) / int(b)
                print(f"The result is {result}")
            else:                
                print(colored("You cannot divide by zero !", "black", "on_red"))
        
        case _:
            print(colored("Option Invalide", "black", "on_red"))

