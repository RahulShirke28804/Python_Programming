'''
    This version uses the if __name__ == "__main__" condition to control program execution. 
    It ensures the main() function runs only when the file is executed directly, 
    not when imported as a module.
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

# Starter
if __name__ == "__main__":
    main()