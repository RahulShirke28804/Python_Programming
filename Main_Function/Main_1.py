'''
    This program organizes the logic using a main() function. It takes two numbers as input, 
    calls a multiplication function, and prints the result, demonstrating basic program 
    structure and function calls in Python.
'''

def Multiplication(Value1, Value2):
    Ans = 0     # Local variable
    Ans = Value1 * Value2
    return Ans

def main():
    No1 = 0
    No2 = 0
    Restult = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = Multiplication(No1,No2)
    print("Multiplication is : ",Result)

main()
