'''
Q.8. Write a Python program to input a string that is a list of words separated by commas. Construct a dictionary that contains all these words as keys and their frequencies as values. Then display the words with their quantities.
'''

str1 = input("Enter String : ")
list1 = str1.split(",")
dict1 = {}
n = (len(list1))
i = 0
while i<n:
    count = list1.count(list1[i])
    dict1[list1[i]] = count
    i += 1
    
print("Input : ",str1)
print("Output : ",dict1)


