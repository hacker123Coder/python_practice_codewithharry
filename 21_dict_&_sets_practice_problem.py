# Q1
# myDict={
#     "kitab" : "book",
#     "kalam" : "pen",
#     "ghadi" : "clock"
# }

# print("options are:", myDict.keys())

# a = input("enter the word to be searched ")
# print("meaning of the word is:", myDict[a])

#Q3

# a = {1, 2, 18, "18", 4} # 18 and "18" are unique values coz of its data type
# print(a)

# Q4

# s = set()     # this is an empty set   
# s.add(20)     # extra space in starting is giving an error
# s.add(20.0)
# s.add("20")

# print(len(s))

# Q6

l1 = input("enter a language akash :")
l2 = input("enter a language piyush :")
l3 = input("enter a language akriti:")
l4 = input("enter a language ram:")

name={"akash" : l1,   # duplicate values are allowed 
"piyush" : l2,
"akriti" : l3,
"ram" : l4
}

name={"ram" : l1,    # duplicate keys are not allowed
"piyush" : l2,
"akriti" : l3,
"ram" : l4
}

print(name)



