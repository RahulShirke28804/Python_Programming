'''
    Creating a Custom Module

Defines constants and functions inside a custom module and uses __name__ to identify module execution context.

'''

PI = 3.14
print("Inside Module : ",__name__)

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Sub(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

