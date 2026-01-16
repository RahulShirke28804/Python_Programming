'''
    Dynamic List Summation (With Function)
Uses a separate function to calculate the sum of dynamically entered list elements.
Each program isolates one idea—input handling, lists, iteration, or functions—keeping the logic clean and
'''

def Summation(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    
    return Sum


def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of elements : ")
    Size = int(input())
    
    Data = list()

    print("Enter the elements : ")
    
    for i in range(Size):
        Value = int(input())
        Data.append(Value)    

    Ret = Summation(Data)

    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()