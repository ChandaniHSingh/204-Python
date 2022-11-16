'''
Q.4. Write a Python program to input 3 numbers and find the largest. Print all the numbers, and the largest
among them, with appropriate titles.
'''

#largest number
num1 = int(input('Enter Number 1 : '))
num2 = int(input('Enter Number 2 : '))
num3 = int(input('Enter Number 3 : '))
if num1 > num2 and num1 > num3:
    large = num1
else:
    if num2 > num3:
        large = num2
    else:
        large = num3
print('All Numbers are : ',num1,num2,num3)
print('Larget Number : ',large)
