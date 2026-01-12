'''
    This program defines a function that multiplies two numbers and returns the result. 
    The function is called from the main program, and the returned value is printed.
'''

def Multiplication(Value1, Value2):
    Ans = 0     # Local variable
    Ans = Value1 * Value2
    return Ans

print("Demo application")

iRet = Multiplication(10,11)
print(iRet)
