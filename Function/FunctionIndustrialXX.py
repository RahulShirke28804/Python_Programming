# Procedural
'''
    Checks whether a number is even or odd using a procedural function that 
    returns a boolean value and evaluates it in main().
'''


def CheckEven(No):
    return((No % 2) == 0)

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckEven(Value)

    print(Ret)
 
    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")
        
if __name__ == "__main__":
    main()