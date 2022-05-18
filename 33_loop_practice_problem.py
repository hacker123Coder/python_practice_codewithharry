# Q1
# num = int(input("enter the number:"))
#  Using for loop
# i = 1
# for i in range (1, 11):
#     print(num * i)
#     print(f"{num} X {i} = {num * i}")   # "F" string
#      i+=1

# Q3
# Using while loop
# i = 1
# while i<11:
#     print(num * i)
#     i = i+1

# Q2
# list = ["harry", "sejal", "sanju"]
# for i in list:
#     if i.startswith('s'):
#         print("hello",i)
#     else:
#         pass
# Q4
# num = int(input("enter a number: "))
# for i in range (2, num):
#     if(num%i == 0):
#         print(f"{num} is not a prime no")
#         break
    
# else:
        #  print(f"{num} is a prime number")
# Q5

# num = int(input("enter a number: "))
# sum = 0
# for i in range(1, num):
#     sum = sum + i
    
# print(sum)

# Q6

# num = int(input("enter a no. :"))
# fact =1
# for i in range(1, num):
#     fact = fact * num
#     num = num-1
# print(fact)


# Q10(reverse table)
num = int(input("enter the number:"))
end = int(input("enter the number:"))


for i in range (1, 11):
    print(num * end)
    end = end-1
    
