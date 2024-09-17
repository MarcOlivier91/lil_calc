from termcolor import colored

def inputs() :  
    print(colored("\nSelect the desired operation with the corresponding letter, then press enter : \n", "green"))    
    print(colored("[A] Add  ", "black", 'on_white'))
    print(colored("[B] Substract  ", "black", "on_white"))
    print(colored("[C] Multiply  ", "black", "on_white"))
    print(colored("[D] Divide  ","black", "on_white"))
    print(colored("[F] Close program  ","black", "on_white"))
