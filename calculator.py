def calculator(a,b):
    a = float(input("enter the first number:"))
    b = float(input("enter the second number:"))
    print("1. addtion[+] , 2. subtraction[-] , 3. multiplication[*] , 4. division[/]")
    c = int(input("enter the desired number for operator"))
    if c== 1 :
        return a+b
    elif c== 2:
        return a-b
    elif c== 3:
        return a*b
    elif c== 4:
        try:
            print(a/b)
        except:
            print("invalid input")
    
    calculator(a,b)