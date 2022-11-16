'''
Q.4. Write a Python program to take input of a positive number, say N, with an appropriate
prompt, from the user. The user should be prompted again to enter the number until the user
enters a positive number. Find the sum of first N odd numbers and first N even numbers.
Display both the sums with appropriate titles.
'''

num = 0
while(True):
    num = input("Enter Positive Number : ")
    if num.isnumeric():
        num = int(num)
        break
    else:
        print("please enter positive numbers only....")
sumEven = 0
sumOdd = 0
i=2
j=1
for k in range(num):
    sumEven = sumEven + i
    i = i + 2
    sumOdd += j
    j +=2
print("Sum Of ", num ,"Even Numbers: ",sumEven)
print("Sum Of ", num ,"Odd Numbers: ",sumOdd)
    
        
    
