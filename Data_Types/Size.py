'''
    This program uses the sys module to check the memory size (in bytes) 
    occupied by different data types such as int, float, and str.
'''

import sys

No = 9497379929238094920348374203874730298347       # int

Marks = 90.90       # float

Name = "Rahul"      # str

print(sys.getsizeof(No))
print(sys.getsizeof(Marks))
print(sys.getsizeof(Name))
