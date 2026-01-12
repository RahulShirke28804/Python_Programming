'''
    This program accepts two numbers from the user, passes them to a multiplication function, 
    and prints the result. It demonstrates user input handling, type conversion, and function 
    reuse.
'''


def Multiplication(Value1, Value2):
    Ans = 0     # Local variable
    Ans = Value1 * Value2
    return Ans

No1 = 0
No2 = 0
Restult = 0

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Result = Multiplication(No1,No2)
print("Multiplication is : ",Result)

##################################################

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Result = Multiplication(No1,No2)
print("Multiplication is : ",Result)