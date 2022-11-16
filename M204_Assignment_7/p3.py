'''
Q.3. Consider a 4 x 3 NumPy array and a 3 x 4 NumPy array. Write a Python program to
perform the Matrix Multiplication of these two NumPy arrays. DO NOT USE THE
BUILT-IN OPERATOR TO FIND THE MATRIX MULTIPLICATION.
'''

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,0,1,2])
print(arr)

arr1 = arr.reshape(4,3)
arr2 = arr.reshape(3,4)
print("Array-1 : ",arr1)
print("Array-2 : ",arr2)

arr3 = np.zeros([4,4],dtype=int)
for i in range(4):
    for j in range(4):
        arr3[i,j] = 0
        for k in range(3):
            arr3[i,j] += arr1[i,k] * arr2[k,j]
            

print("Multiplcation : ")
print(arr3)
