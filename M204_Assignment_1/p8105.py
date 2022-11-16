'''
Q.8. Write a Python program to input 3 numbers and find the largest. Print all the numbers, and the largest
among them, with appropriate titles. Display appropriate message and exit from the program if any of
these inputs is not a numeric value.
'''

#largest number with exit condition


#using isnumeric [list]

large = 0
num_list = []
for i in range(1,4):
    val = input('Enter Number : ')
    if val.isnumeric():
        val = int(val)
    else:
        ValueError : print("This is Not Numeric Type")
        exit()
    num_list.append(val)
    if large<val:
        large = val
print('All Numbers : ',num_list)
print('Largest Number : ',large) 

#using try...except [list]
'''
large = 0
num_list = []
for i in range(1,4):
    val = input('Enter Number : ')
    try:
        val = int(val)
    except:
        ValueError : print("This is Not Numeric Type")
        exit()
    num_list.append(val)
    if large<val:
        large = val
print('All Numbers : ',num_list)
print('Largest Number : ',large) 
 '''

# using isnumeric
'''
num1 = input('Enter Number 1 : ')
if num1.isnumeric():
    int(num1)
else:
    print("This is Not Numberic value")
    exit()
num2 = input('Enter Number 2 : ')
if num2.isnumeric():
    int(num2)
else:
    print("This is Not Numberic value")
    exit()
num3 = input('Enter Number 3 : ')
if num3.isnumeric():
    int(num3)
else:
    print("This is Not Numberic value")
    exit()
if num1 > num2 and num1 > num3:
    large = num1
else:
    if num2 > num3:
        large = num2
    else:
        large = num3
print('All Numbers are : ',num1,num2,num3)
print('Larget Number : ',large)
'''



#using try...except
'''
num1 = input('Enter Number 1 : ')
try:
    num1 = int(num1)
except:
    ValueError : print("This is Not Numberic value")
    quit()
num2 = input('Enter Number 2 : ')
try:
    num2 = int(num2)
except:
    ValueError : print("This is Not Numberic value")
    quit()
num3 = input('Enter Number 3 : ')
try:
    num3 = int(num3)
except:
    ValueError : print("This is Not Numberic value")
    quit()
if num1 > num2 and num1 > num3:
    large = num1
else:
    if num2 > num3:
        large = num2
    else:
        large = num3
print('All Numbers are : ',num1,num2,num3)
print('Larget Number : ',large)
'''
#using break
'''
large = 0
num_list = []
for i in range(1,4):
    val = input('Enter Number : ')
    if val.isnumeric():
        val = int(val)
    else:
        ValueError : print("This is Not Numeric Type")
        break
    num_list.append(val)
    if large<val:
        large = val
print('All Numbers : ',num_list)
print('Largest Number : ',large) 
'''
