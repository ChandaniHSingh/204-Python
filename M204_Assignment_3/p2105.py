'''
Q.2. Write a Python program to create a list of lists of numbers (i.e. each element of the list is a list of numbers e.g. [[1, 2], [3, 2, 5], [1], [5, 3, 6, 7]]. Then generate a list from the given list where each element of the list is the length of each list in the given list. i.e. for the given example the output should be [2, 3, 1, 4]. You can take input of non-zero numbers, with an appropriate prompt, from the user until the user enters a zero to create the list assuming that the numbers are non-zero.
Sample Input: [[1, 2], [3, 2, 5], [1], [5, 3, 6, 7]]
Output: [2, 3, 1, 4]
'''

list1 = []
anslist1 = []
while True:
    take = input("\nEnter Y or y to enter new list :  ")
    try:
        take = str(take)
        take = take[0]
        if take == 'y' or take == 'Y':
            templist = []
            while True:
                print("Enter 0 (zero) to STOP Current list...")
                num = input("Enter Number : ")
                try:
                    num = int(num)
                    if num == 0:
                        break
                    templist.append(num)
                except:
                    print("Please enter Numbers Only...")
                    
            list1.append(templist)
            anslist1.append(len(templist))
        else:
            print("Terminated...")
            break
    except:
        print("Please enter Y to continue..")
    
print("Input : ",list1)
print("Size of Each List Element : ",anslist1)

      

