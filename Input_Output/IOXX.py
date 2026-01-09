'''
    This program shows that values received from input() 
    are strings by default, then converts them to integers 
    using int() to perform addition.
'''


print("Enter first number : ")
No1 = input()

print("Enter first number : ")
No2 = input()

print(type(No1))
print(type(No2))

Ans = int(No1) + int(No2)

print(type(No1))
print(type(No2))

print("Addition is : ",Ans)
