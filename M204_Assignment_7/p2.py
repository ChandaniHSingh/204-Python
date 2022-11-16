'''
Q.2. Consider a 1-D NumPy array of 10 elements, where each element is temperature in
degrees Celsius. Write a Python program to Convert it to an array containing temperature
in degrees Fahrenheit. The relation between Celsius and Fahrenheit is C / 5 = (F – 32) /
9. Display them in an appropriate format.
'''

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])

print("In Celsius : ")
print(arr)

for i in range(10):
    arr[i] = (arr[i]*(9/5))+32

print("In Fahrenheit : ")
print(arr)


