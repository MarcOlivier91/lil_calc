from termcolor import colored

def operationChoice() : 
    a = input("Choose your first number : \n")
    b = input("Choose your second number : \n")
    print(colored("\nSelect the desired operation : \n", "green"))
    print(colored("[A] Add  ", "black", 'on_white'))
    print(colored("[B] Substract  ", "black", "on_white"))
    print(colored("[C] Multiply  ", "black", "on_white"))
    print(colored("[D] Divide  ","black", "on_white"))