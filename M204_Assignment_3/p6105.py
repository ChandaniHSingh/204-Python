'''
Q.6. Write a Python program to take input of a string from the user and then create a dictionary containing each character of the string along with their frequencies. (e.g. if the string is ‘banana’ then output should be {'b': 1, 'a': 3, 'n': 2}.
'''

dict1 = {}
str1 = input("\nEnter String : ")
for i in range(len(str1)):
    n = str1[i]
    dict1[n]=str1.count(n)

print("Input : ",str1)
print("Output : ",dict1)


