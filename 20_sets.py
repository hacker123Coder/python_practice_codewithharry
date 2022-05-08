a={9, 9, 0, 4}
print(a)    #sets do not allow duplicate values
print(type(a))

a.add((3, 4, 5)) #can add tuples to sets coz it cannot be changed
print(a)

a.add({3:9}) # cannot add dictionary and lists to set as it can be changed 
print(a)

print(len(a)) # prints the length of set 

a.remove(9)
print(a)