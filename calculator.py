def add():
    #Adds two inputs together
    a = int(input(f"Enter the first number: "))
    print(f"+")
    b = int(input(f"Enter the second number: "))
    ans = a + b
    print(f"Answer = {a} + {b} = {ans}\n")

def subtract():
    #Subtracts two inputs together
    a = int(input(f"Enter the first number: "))
    print(f"-")
    b = int(input(f"Enter the second number: "))
    ans = a - b
    print(f"Answer = {a} - {b} = {ans}\n")

def multiply():
    #multiplies two inputs together
    a = int(input(f"Enter the first number: "))
    print(f"x")
    b = int(input(f"Enter the second number: "))
    ans = a * b
    print(f"Answer = {a} x {b} = {ans}\n")

def divide():
    #divides first input by second input
    a = int(input(f"Enter the first number: "))
    print(f"/")
    b = int(input(f"Enter the second number: "))
    ans = int(a / b)
    print(f"Answer = {a} / {b} = {ans}\n")

def exponent():
    #raises first input by second input
    a = int(input(f"Enter the first number: "))
    print(f"^")
    b = int(input(f"Enter the second number: "))
    ans = a ** b
    print(f"Answer = {a} ^ {b} = {ans}\n")

print(f"Enter '0' to quit at any time")
while True:
    print("""\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponent""")
    try:
        operation = int(input("Which operation would you like to use:"))
        if operation == 1:
            add()
            cont = input(f"Would you like to continue(Y/N):")
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                print(f"Thank you for using this program.")
                break
        
        elif operation == 2:
            subtract()
            cont = input(f"Would you like to continue(Y/N):")
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                print(f"Thank you for using this program.")
                break
        
        elif operation == 3:
            multiply()
            cont = input(f"Would you like to continue(Y/N):")
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                print(f"Thank you for using this program.")
                break
        
        elif operation == 4:
            divide()
            cont = input(f"Would you like to continue(Y/N):")
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                print(f"Thank you for using this program.")
                break
        
        elif operation == 5:
            exponent()
            cont = input(f"Would you like to continue(Y/N):")
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                print(f"Thank you for using this program.")
                break
        
        else:
            break

            
    except ValueError:
        print(f"\nEnter either one of the displayed numbers(1-5)\n")

