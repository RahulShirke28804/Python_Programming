'''
    This code checks the value of __name__ and prints whether the file is running 
    as a standalone program or being used as a module, explaining Python’s execution context.
'''

if __name__ == "__main__":
    print("Self executable file")
else:
    print("Module file")
    