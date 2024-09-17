from termcolor import colored

def inputs() :  
    print(colored("\nSelect the desired operation with the corresponding number, then press enter : \n", "green"))    
    print(colored("[1] Add  ", "black", 'on_white'))
    print(colored("[2] Substract  ", "black", "on_white"))
    print(colored("[3] Multiply  ", "black", "on_white"))
    print(colored("[4] Divide  ","black", "on_white"))
    print(colored("[9] Close program  ","black", "on_white"))
