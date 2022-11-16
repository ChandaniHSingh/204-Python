'''
Q.3. Create a list of numbers. Then divide the list into 3 parts and reverse each part. Display all the
parts.
'''

import math

lst = []

while True:
    val = int(input("Enter Number : "))
    if val == 0:
        break
    lst.append(val)


#Divide in 3 part
    
if(len(lst) < 3):
    print("can't divide in 3 part..because less that 3 elements....")
    exit()
else:
    div = math.ceil(len(lst)/3)
    #div = (len(lst)//3)
    lst1 = lst[0:div]
    lst2 = lst[div:div+div]
    lst3 = lst[div+div:]

print(lst1)
print(lst2)
print(lst3)


#Reverse Each Part

lst1 = lst1[::-1]
lst2 = lst2[::-1]
lst3 = lst3[::-1]

print(lst1)
print(lst2)
print(lst3)

