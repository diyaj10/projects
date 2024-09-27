def calculator(a,b):
    a = float(input("enter the first number:"))
    b = float(input("enter the second number:"))
    c = input("enter the operator you want to apply ( +, - , * , / )")
    if c=='+' :
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        try:
            print(a/b)
        except:
            print("invalid input")
    
    calculator(a,b)
