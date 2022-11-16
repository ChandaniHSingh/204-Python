'''
Q.3. Write a Python program to create a list of numbers by taking input from the user. Split this list into two tuples where one tuple contains odd numbers, and the other tuple contains even numbers from the list. You can take input of non-zero numbers, with an appropriate prompt, from the user until the user enters a zero to create the list assuming that the numbers are nonzero.
Sample Input: [10, 12, 13, 90, 43, 32, 30, 11]
Output:
Tuple of Odd Numbers: (13, 43, 11)
Tuple of Even Numbers: (10, 12, 90, 32, 30)
'''

def funOdd():
    listOdd = []
    for i in list1:
        if i % 2 != 0:
            listOdd.append(i)
    return tuple(listOdd)

def funEven():
    listEven = []
    for i in list1:
        if i % 2 == 0:
            listEven.append(i)
    return tuple(listEven)

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
print("Tuple of Odd Numbers : ",funOdd())
print("Tuple of Even Numbers : ",funEven())
          

      
