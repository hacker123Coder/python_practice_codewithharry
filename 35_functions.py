# def func():                 # write once call many times
#     print("hello")

# func()          
# func()
# func()
# func()
# func()

# Ex-2

def add(num):
   return ( num[0] + num[1] + num[2] )

num1=[1,2,3]

total1 = add(num1)
print(total1)

num2=[2,2,3]

total2=add(num2)
print(total2)

if(total1>total2):
    print("total 1 is greater")
else:
    print("total 2 is greater")