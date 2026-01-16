'''
    Dynamic List Input
Accepts a list of numbers from the user at runtime and displays the list.
'''

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())
    
    Data = list()

    print("Enter the elements : ")
    
    for i in range(Size):
        Value = int(input())
        Data.append(Value)    
    print(Data)

if __name__ == "__main__":
    main()