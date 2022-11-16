'''
Q.1. Consider a 4 x 4 NumPy array of your choice. Write a Python program that finds the
following and display them in an appropriate format for the given NumPy array: (NOTE:
DO NOT USE BUILT-IN FUNCTIONS TO FIND THE MAXIMUM, MINIMUM
AND SUM)
 Maximum, Minimum and Sum of all the elements of the matrix
 Maximum, Minimum and Sum of all the elements of each row
 Maximum, Minimum and Sum of all the elements of each column
 Maximum, Minimum and Sum of all the diagonal elements.
'''

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,0,6,5,4,3,2,1])

print(arr)

arr2 = arr.reshape(4,4)
print(arr2)


print("\nMaximum, Minimum and Sum of all the elements of the matrix :\n--------------------------------------------------------\n")
asum = 0
amin = arr2[0,0]
amax = arr2[0,0]
for i in range(4):
    for j in range(4):
        asum = asum + arr2[i,j]
        if(amin > arr2[i,j]):
            amin = arr2[i,j]
        if(amax < arr2[i,j]):
            amax = arr2[i,j]

print("Maximum : ",amax)
print("Minimum : ",amin)
print("Sum : ",asum)

print("\nMaximum, Minimum and Sum of all the elements of each Row :\n--------------------------------------------------------\n")

for i in range(4):
    asum = 0
    amin = arr2[i,0]
    amax = arr2[i,0]
    for j in range(4):
        asum = asum + arr2[i,j]
        if(amin > arr2[i,j]):
            amin = arr2[i,j]
        if(amax < arr2[i,j]):
            amax = arr2[i,j]
    print("Row No. : ",i+1)
    print("Maximum : ",amax)
    print("Minimum : ",amin)
    print("Sum : ",asum)

print("\nMaximum, Minimum and Sum of all the elements of each Column :\n--------------------------------------------------------\n")

for j in range(4):
    asum = 0
    amin = arr2[0,j]
    amax = arr2[0,j]
    for i in range(4):
        asum = asum + arr2[i,j]
        if(amin > arr2[i,j]):
            amin = arr2[i,j]
        if(amax < arr2[i,j]):
            amax = arr2[i,j]
    print("Column No. : ",j+1)
    print("Maximum : ",amax)
    print("Minimum : ",amin)
    print("Sum : ",asum)

print("\nMaximum, Minimum and Sum of all the elements of All Diagonal :\n--------------------------------------------------------\n")

asum = 0
amin = arr2[0,0]
amax = arr2[0,0]
for i in range(4):
    for j in range(4):
        if(i == j):
            asum = asum + arr2[i,j]
            if(amin > arr2[i,j]):
                amin = arr2[i,j]
            if(amax < arr2[i,j]):
                amax = arr2[i,j]
print("Diagonal No. : ",1)
print("Maximum : ",amax)
print("Minimum : ",amin)
print("Sum : ",asum)

asum = 0
amin = arr2[0,0]
amax = arr2[0,0]
for i in range(4):
    for j in range(4):
        if(i == 4-j-1):
            asum = asum + arr2[i,j]
            if(amin > arr2[i,j]):
                amin = arr2[i,j]
            if(amax < arr2[i,j]):
                amax = arr2[i,j]
print("Diagonal No. : ",2)
print("Maximum : ",amax)
print("Minimum : ",amin)
print("Sum : ",asum)
    

