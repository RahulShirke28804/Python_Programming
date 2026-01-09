'''
    This program shows that dictionary values can be modified 
    by assigning a new value to an existing key.
'''


Information = {"Name" : "Rahul", "Age" : 25, "City" : "Pune", "Marks" : 89.90}
print(type(Information))
print(Information)

print(Information["City"])
Information["Age"] = 26

print(Information)
