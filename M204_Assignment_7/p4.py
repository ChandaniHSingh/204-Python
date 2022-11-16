'''
Q.4. Consider a NumPy array where each row represents data of a student and there are 10
such rows. The data of a student consists of rollno, name, city and age. i.e. each row
contains rollno, name, city and age of a student. Write a Python program to find the
following:
 Maximum, Minimum and Average age of all the students
 Maximum, Minimum and Average age of all the students living in a particular
city (take input of name of a city from the user)
 Maximum, Minimum and Average age of all the students whose name starts
with the letter ‘A’
 Maximum, Minimum and Average age of all the students having rollno > n (take
input of n from the user)
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

print("\nMaximum, Minimum and Average age of all the students\n---------------------------------------------------\n")
amin = 0
amax = 0
asum = 0
for i in range(10):
    if(int(arr[i,3]) < amin):
        amin = int(arr[i,3])
    if(int(arr[i,3]) > amax):
        amax = int(arr[i,3])
    asum = asum + int(arr[i,3])

print("Maximum age : ",amax)
print("Minimum age : ",amin)
print("Average age : ",asum/10)

print("\nMaximum, Minimum and Average age of all the students living in a particular city (take input of name of a city from the user)\n---------------------------------------------------\n")

city = input("ENter City : ").strip()

amin = 0
amax = 0
asum = 0
count = 0
for i in range(10):
    if(arr[i,2] == city):
        count += 1
        if(count == 1):
            amin = int(arr[i,3])
            amax = int(arr[i,3])
        if(int(arr[i,3]) < amin):
            amin = int(arr[i,3])
        if(int(arr[i,3]) > amax):
            amax = int(arr[i,3])
        asum = asum + int(arr[i,3])
        
if(count != 0):
    print("Maximum age : ",amax)
    print("Minimum age : ",amin)
    print("Average age : ",asum/count)
else:
    print("No Record Found")

print("\nMaximum, Minimum and Average age of all the students whose name starts with the letter ‘A’\n---------------------------------------------------\n")

amin = 0
amax = 0
asum = 0
count = 0
for i in range(10):
    if(arr[i,1].startswith("A")):
        count += 1
        if(count == 1):
            amin = int(arr[i,3])
            amax = int(arr[i,3])
        if(int(arr[i,3]) < amin):
            amin = int(arr[i,3])
        if(int(arr[i,3]) > amax):
            amax = int(arr[i,3])
        asum = asum + int(arr[i,3])

if(count != 0):
    print("Maximum age : ",amax)
    print("Minimum age : ",amin)
    print("Average age : ",asum/count)
else:
    print("No Record Found")


print("\nMaximum, Minimum and Average age of all the students having rollno > n (take input of n from the user))\n---------------------------------------------------\n")

rollno = int(input("ENter N : "))

amin = 0
amax = 0
asum = 0
count = 0
for i in range(10):
    if(int(arr[i,0]) > rollno):
        count += 1
        if(count == 1):
            amin = int(arr[i,3])
            amax = int(arr[i,3])
        if(int(arr[i,3]) < amin):
            amin = int(arr[i,3])
        if(int(arr[i,3]) > amax):
            amax = int(arr[i,3])
        asum = asum + int(arr[i,3])
        
if(count != 0):
    print("Maximum age : ",amax)
    print("Minimum age : ",amin)
    print("Average age : ",asum/count)
else:
    print("No Record Found")

