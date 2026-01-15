# Procedural

'''
    Checks whether a number is even or odd using a function that returns 
    a boolean value, followed by conditional output in main().
'''
def CheckEven(No):
    if((No % 2) == 0):
        print("It is Even")
    else:
        print("It is Odd")    

Value = 0

print("Enter number : ")
Value = int(input())

CheckEven(Value)
