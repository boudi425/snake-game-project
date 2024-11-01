num1=float(input("enter a number "))
num2=float(input("enter a number "))
operator=input("enter the operator ")

def ope1(num1, operator, num2):
    print(eval(f"{num1} {operator} {num2}"))
    


ope1(num1=num1, operator=operator, num2=num2)