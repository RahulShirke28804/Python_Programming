'''
    Implements an even-number check using a function that returns True or False 
    and prints the result without additional conditional messages.
'''

def CheckEven(No):
    if((No % 2) == 0):
        print("It is Even")
    else:
        print("It is Odd")    

def main():
    CheckEven(21)               # Positional    
    CheckEven(No = 22)          # Keyword

if __name__ == "__main__":
    main()