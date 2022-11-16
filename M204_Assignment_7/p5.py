'''
Q.5. Consider the NumPy array used in Q.4. Write a Python program to do the following:
 Display details of all the students living in a particular city (take input of name
of a city from the user) in appropriate format
 Display details of all the students having age greater than N (take input of N
from the user) in appropriate format
'''

import numpy as np
arr = np.zeros([10,4],dtype=object)

arr[0] = np.array([1,"Chandani","Surat",21])
arr[1] = np.array([2,"Sumit","Surat",23])
arr[2] = np.array([3,"Saloni","Ahemdabad",23])
arr[3] = np.array([4,"Aakansha","Ahemdabad",21])
arr[4] = np.array([5,"Khushi","Banglore",15])
arr[5] = np.array([6,"Harendra","Surat",48])
arr[6] = np.array([7,"Seema","Surat",50])
arr[7] = np.array([8,"Vijay","Surat",21])
arr[8] = np.array([9,"Aman","Hydrabad",23])
arr[9] = np.array([10,"Shibu","Patan",27])


print(arr)

print("\nDisplay details of all the students\n---------------------------------------------------\n")
print("RollNo   Name     City   Age\n---------------------------------------------------\n")
for i in range(10):
    print(arr[i,0],"   ",arr[i,1],"   ",arr[i,2],"   ",arr[i,3])


print("\nDisplay details of all the students living in a particular city (take input of name of a city from the user) in appropriate format\n---------------------------------------------------\n")

city = input("ENter City : ").strip()

count = 0

print("RollNo   Name     City   Age\n---------------------------------------------------\n")
for i in range(10):
    if(arr[i,2] == city):
        print(arr[i,0],"   ",arr[i,1],"   ",arr[i,2],"   ",arr[i,3])
        count += 1

if(count == 0):
    print("No Record Found")


print("\nDisplay details of all the students having age greater than N (take input of N from the user) in appropriate format\n---------------------------------------------------\n")

rollno = int(input("ENter N : "))

count = 0

print("RollNo   Name     City   Age\n---------------------------------------------------\n")
for i in range(10):
    if(int(arr[i,0]) > rollno):
        print(arr[i,0],"   ",arr[i,1],"   ",arr[i,2],"   ",arr[i,3])
        count += 1

if(count == 0):
    print("No Record Found")

