'''
    Importing and Using a Custom Module

Demonstrates how to import a user-defined module and access its variables and functions.
'''

import Marvellous

print("Inside client : ",__name__)

print("Value of PI is : ",Marvellous.PI)

Result = 0

Result = Marvellous.Add(11,10)
print("Addition is : ",Result)

Result = Marvellous.Sub(11,10)
print("Substraction is : ",Result)