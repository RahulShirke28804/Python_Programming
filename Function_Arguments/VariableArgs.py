'''
    Variable Length Arguments (*args)
    Shows how a function can accept any number of arguments using *args, which are stored as a tuple.
'''

def Addition(*No):
   print(No) 
   print(type(No))      # tuple
   print(len(No))       

def main():
    Addition(11,21,51,101,11)

if __name__ == "__main__":
    main()  