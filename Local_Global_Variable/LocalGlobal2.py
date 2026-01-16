'''
    Explains how a function can read a global variable without modifying it.
'''

No = 11         # Global

def Fun():
    print("Value of No from Fun is : ",No)      # 11

print("Value of No is : ",No)                   # 11
Fun()