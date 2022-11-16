'''
Q.1. Write a Python program to create a list of numbers by taking input from the user and then remove the duplicates from the list. You can take input of non-zero numbers, with an appropriate prompt, from the user until the user enters a zero to create the list assuming that the numbers are non-zero.
Sample Input: [10, 34, 18, 10, 12, 34, 18, 20, 25, 20]
Output: [10, 34, 18, 12, 20, 25]
'''

#By Using Convert list to set
list1 = []
while True:
    num = input("Enter Number : ")
    try:
        num = int(num)
        if num == 0:
            break
        list1.append(num)
    except:
        print("Please enter Numbers Only...")
    finally:
        print("Enter 0 (zero) to STOP...")

print("Input : ",list1)
set1 = set(list1)
anslist1 = list(set1)
print("Output : ",anslist1)

'''
#Check each time item exists or not
list1 = []
anslist1 = []
while True:
    num = input("Enter Number : ")
    try:
        num = int(num)
        if num == 0:
            break
        if num not in list1:
            anslist1.append(num)
        list1.append(num)
    except:
        print("Please enter Numbers Only...")
    finally:
        print("Enter 0 (zero) to STOP...")

print("Input : ",list1)
print("Output : ",anslist1)
'''

          
