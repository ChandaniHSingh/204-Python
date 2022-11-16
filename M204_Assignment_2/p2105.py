'''
Q.2. Write a Python program to take input of positive numbers, with an appropriate prompt, from
the user until the user enters a zero. Find total number of odd & even numbers entered and
sum of odd and even numbers. Display total count of odd & even numbers and sum of odd
& even numbers with appropriate titles.
'''

countOdd = 0
sumOdd = 0
countEven = 0
sumEven = 0
while(True):
    print("Enter 0 to stop.")
    num = input("Enter Positive Number : ")
    if num.isnumeric():
        num = int(num)
        if (num == 0):
            break
        if (num%2 == 0):
            countEven += 1
            sumEven += num
        else:
            countOdd += 1
            sumOdd += num
    else:
        print("please enter positive numbers only....")
print("Count Of Even Numbers : ",countEven)
print("Sum Of Even Numbers: ",sumEven)
print("Count Of Odd Numbers : ",countOdd)
print("Sum Of Odd Numbers: ",sumOdd)
