from termcolor import colored


def calculator():    
    a = input('Enter first number : ')
    b = input('Enter second number: ')
    operation = input("Select the operation : \n A) Add \n B) Substract \n C) Multiply \n D) Divide \n")

    if operation.capitalize() == "A":
        result = float(a) + float(b)
        
    elif operation.capitalize() == "B":
        result = float(a) - float(b)
    
    elif operation.capitalize() == "C":
        result = float(a) * float(b)

    elif operation.capitalize() == "D":
        if float(a) or float(b) == 0:
            print("You cannot divide by zero ! \n")
            exit(0)
            
        result = float(a) / float(b)
            
    print(f"The total is {result}")
    
calculator()