'''
    Fixed Number of Function Arguments
    Demonstrates a function that accepts an exact number of arguments. 
    Shows that Python raises errors when fewer or extra arguments are passed.
'''

def Display(A,B,C,D):
    print(A,B,C,D)


def main():
    # Display(10,20)    Not allowed - Less arguments
    # Display(10,20,30,40,50)       Not allowed - Extra arguments
    Display(10,20,30,40)        # Allowed

if __name__ == "__main__":
    main()  