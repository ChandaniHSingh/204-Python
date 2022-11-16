'''
Q.1. Write a Python program to take input of non-zero numbers, with an appropriate prompt, from
the user until the user enters a zero. Find total number of numbers entered and their sum.
Display count and sum with appropriate titles.
'''

count = 0
sum = 0
while(True):
    print("Enter 0 to stop.")
    num = input("Enter Non-Zero Number : ")
    if num.isnumeric():
        num = int(num)
        if (num == 0):
            break
        count += 1
        sum += num
    else:
        print("please enter numbers only....")
print("Count : ",count)
print("Sum : ",sum)
