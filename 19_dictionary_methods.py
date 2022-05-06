dict = {
    "mr" : "atul",
    "mrs" : "kavya",
    "marks":[34, 60, 50, 89],       
    "dict2":{"money" : "rupees"}    
}

print(type(dict.keys()))
print(dict.keys())          # prints the key of the dictionary
print(dict.values())        # prints the value of the dictionary

print(dict.items ())        #Prints the (key, value) for all contents of the dictionary

updateDict= {
    "insect" : "mosquito"
}

dict.update(updateDict)
print(dict)