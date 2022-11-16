'''
Q.5. Write a Python program to create a dictionary of student data by taking input from the user, where each student data contains Rollno (to be considered as key), and marks in 3 subjects (to be considered as list of values). e.g. {1 : [45, 40, 35], 2 : [41, 38, 39], 3 : [35, 30, 37]}. Prepare mark list in the following format:
Roll No. Mark-1 Mark-2 Mark-3 Total
1 45 40 35 120
'''

dict1 = {}
n = input("\nEnter Number of Student : ")
try:
    n = int(n)
    for i in range(n):
        roll = input("Enter Roll No. : ")
        markList = []
        k=1
        while k<=3:
            num = input("Enter Marks : ")
            try:
                num = int(num)
                markList.append(num)
                k += 1
            except:
                print("Please enter Numbers Only...")                
        dict1[roll] = markList
except:
    print("Please enter Positive Number..")
    
print("Input : ",dict1)
print("Output : ")
print("Roll No. Mark-1 Mark-2 Mark-3 Total")
for i in dict1.items(): 
    print(i[0],end ="\t")
    sum = 0
    for k in i[1]:
        print(k,end ="\t")
        sum += k
    print(sum,end="\t")
    print("\n")

