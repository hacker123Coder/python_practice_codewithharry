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

# Dictionary can be updated..
updateDict= {
    "insect" : "mosquito"
}

dict.update(updateDict)
print(dict)

print(dict.get("insect"))  # this will give the value pair      
print(dict["insect"])      # this will give the value pair   

# difference between get and [] can be find out by giving wrong keys

print(dict.get("insect1"))  # it will give None
print(dict["insect1"])      # it will give an error
