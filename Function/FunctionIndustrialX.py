# Procedural

'''
    Checks whether a user-entered number is even or odd using a procedural approach, 
    where a function returns a boolean value that is evaluated in main().
'''
def CheckEven(No):
    if((No % 2) == 0):
        return True
    else:
        return False    

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