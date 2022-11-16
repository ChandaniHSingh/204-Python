'''
Q.7. Consider a single list consisting of integer values, float values, character values, string
values and lists. Write a Python program to do the following:
1) Count total number of elements in the list
2) Count total number of integer values, float values, character values, string
values and lists
Display all the values with appropriate titles.
'''

def count(charList):
    print("Count : ",len(charList))

def countAll(charList):
    countInt = 0
    countFloat = 0
    countChar = 0
    countStr = 0
    countList = 0
    for i in charList:
        if(isinstance(i,list)):
            countList +=1
        elif(isinstance(i,int)):
            countInt += 1
        elif(isinstance(i,float)):
            countFloat += 1
        elif(isinstance(i,str)):
            if (len(i) == 1):
                countChar += 1
            else:
                countStr += 1
    print("Count of List : ",countList)
    print("Count of Integers : ",countInt)
    print("Count of Floats : ",countFloat)
    print("Count of Characters : ",countChar)
    print("Count of Strings : ",countStr)


        
charList = ['A','$','*',1,2,4.5,6.7,[1,2,3,4],'Chandani','Singh']
count(charList)
countAll(charList)
