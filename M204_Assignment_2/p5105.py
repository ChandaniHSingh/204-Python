'''
Q.5. Consider a list of numbers. Write a Python program to do the following:

1) Count total number of numbers in the list
2) Sum and Average of all the numbers in the list
3) Count and sum of all the odd numbers in the list
4) Count and sum of all the even numbers in the list
5) Find the largest number in the list
6) Find the smallest number in the list
Display all the values with appropriate titles.
'''

def count(numList):
    print("Count : ",len(numList))

def sumAvg(numList):
    sum = 0
    for i in numList:
        sum += i
    avg = sum / len(numList)
    print("Sum : ",sum)
    print("Average : ",avg)

def countSumOdd(numList):
    sum = 0
    count = 0
    for i in numList:
        if (i%2 == 1):
            sum += i
            count += 1
    print("Count Odd Numbers : ",count)
    print("Sum of Odd Numbers : ",sum)

def countSumEven(numList):
    sum = 0
    count = 0
    for i in numList:
        if (i%2 == 0):
            sum += i
            count += 1
    print("Count Even Numbers : ",count)
    print("Sum of Even Numbers : ",sum)

def findMax(numList):
    print("Maximum value in List : ",max(numList))

def findMin(numList):
    print("Minimum value in List : ",min(numList))
          
numList = [1,2,3,4,5,6,7,8,9,10]
count(numList)
sumAvg(numList)
countSumOdd(numList)
countSumEven(numList)
findMax(numList)
findMin(numList)
