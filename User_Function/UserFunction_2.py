'''
    This program defines a multiplication function and uses predefined values in the main program. 
    It demonstrates function calling, local variables, and returning a result.
'''

def Multiplication(Value1, Value2):
    Ans = 0     # Local variable
    Ans = Value1 * Value2
    return Ans

print("Demo application")

No1 = 10
No2 = 11
Result = 0

Result = Multiplication(No1,No2)
print("Multiplication is : ",Result)