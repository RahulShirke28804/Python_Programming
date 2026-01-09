'''
    This program shows that:

    bytes are indexed and ordered

    They are immutable (cannot be modified after creation)
'''

# Indexed
# Ordered
# Immutable

Data = bytes([65,97,98])

print(Data)
print(type(Data))
print(Data[0])

# Data[0] = 66      Error
print(Data[0])