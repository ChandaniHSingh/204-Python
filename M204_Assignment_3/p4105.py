'''
Q.4. Write a Python program to create a list of elements of any data type (mixed data type, i.e. some elements maybe of type int, some elements of type float and some elements of type string). Split this list into three tuples containing elements of same data type (i.e. 1st tuple of integers only, 2nd tuple of float only and 3rd tuple of strings only). Take input from the user to create the list.
Sample Input: [25, 4.5, ‘Hello’, 90, 20, 7.5, 9.25, ‘World’]
Output:
Tuple of Integers: (25, 90, 20)
Tuple of Float Values: (4.5, 7.5, 9.25)
Tuple of Strings: (‘Hello’, ‘World’)
'''

list1 = []
listInt = []
listFloat = []
listStr = []
while True:
    num = input("Enter Input : ")
    try:
        if num == "0":
            break
        try:
            num = int(num)
            listInt.append(num)
        except:  
            try:
                num = float(num)
                listFloat.append(num)
            except:
                num = str(num)
                listStr.append(num)
        list1.append(num)
    except:
        print("Please enter Valid Input Only...")
    finally:
        print("Enter 0 (zero) to STOP...")

print("Input : ",list1)
print("List of Integers : ",tuple(listInt))
print("List of Float Values : ",tuple(listFloat))
print("List of Strings : ",tuple(listStr))


               
