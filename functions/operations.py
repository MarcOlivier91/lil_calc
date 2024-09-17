from termcolor import colored
import os
from time import sleep
from functions.inputs import *

def operations() :     
    operationChoice = input()
    os.system('cls')
    a = int(input(colored("Choose your first number : ", "white", "on_blue")))
    b = int(input(colored("Choose your second number : ", "white", "on_blue")))    


    while operationChoice.capitalize() != "F":
        if operationChoice.capitalize() == "A" :
            result = float(a) + float(b)
            print(f"The result is {result}")
        
        if operationChoice.capitalize() == "B" :
            result = float(a) - float(b)
            print(f"The result is {result}")
        
        if operationChoice.capitalize == "C" :
            result = float(a) * float(b)
            print(f"The result is {result}")
            
        if operationChoice.capitalize() == "D" :
            if float(a) or float(b) == 0 :
                print(colored("You cannot divide by zero !", "black", "on_red"))

        sleep(3)
        os.system('cls')

        inputs()
        a = 0
        b = 0
        operationChoice = input()


    print("Bye")
