'''
    This program defines a user-defined function that accepts two numbers, 
    performs addition, returns the result, and prints it after calling the function.
'''

def Addition(No1, No2):
    Ans = None
    Ans = No1 + No2
    return Ans

Result = Addition(10, 11)

print("Addition is : ",Result)
