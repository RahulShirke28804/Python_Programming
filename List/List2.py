'''
        List Traversal and Summation (Static List)
    Iterates through a predefined list and calculates the sum of its elements.
'''

Data  = [10,20,30,40,50]

for i in range(5):
    print(Data[i])


Sum = 0

for i in range(5):
    Sum = Sum + Data[i]

print("Summation is : ",Sum)