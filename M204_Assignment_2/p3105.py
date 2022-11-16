'''
Q.3. Write a Python program to take input of a positive number, with an appropriate prompt, from
the user. The user should be prompted again to enter the number until the user enters a
positive number. Check whether the number is a prime number or not and accordingly
display appropriate message.
'''

num = 0
while(True):
    num = input("Enter Positive Number : ")
    if num.isnumeric():
        num = int(num)
        if num == 0:
            print("please enter > 0 numbers only....")
            continue
        break
    else:
        print("please enter positive numbers only....")
flag = 0
for i in range(2,num):
    if(num%i == 0):
        flag = 1
        break
if (flag == 0):
    print(num ," is Prime Number")
else:
    print(num ," is Not Prime Number")
    
        
    
