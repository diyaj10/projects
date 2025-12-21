def calculator():
    a = float(input("enter the first number:"))
    b = float(input("enter the second number:"))
    print("1. addtion[+] , 2. subtraction[-] , 3. multiplication[*] , 4. division[/]")
    c = int(input("enter the desired number for operator"))
    match c:
        case 1:
            print("the addition is:", a + b)
        case 2:
            print("the subtraction is:", a - b)
        case 3:
            print("the multiplication is:", a * b)
        case 4:
           try:
               print("the division is:", a / b)
           except ZeroDivisionError:
               print("Error: Division by zero is not allowed.")
        case _:
            print("invalid operator")

calculator()