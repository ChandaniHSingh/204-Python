'''
Q.7. Write a Python program to create a list of strings by taking input from the user and then create a dictionary containing each string along with their frequencies. (e.g. if the list is [‘apple’, ‘banana’, ‘fig’, ‘apple’, ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’] then output should be {'apple': 3, 'banana': 2, 'fig': 3, 'grapes': 2}.
'''

list1 = []
dict1 = {}
while True:
    print("Enter 0 to STOP...")
    str1 = input("\nEnter String : ")
    if str1 == "0":
        break
    list1.append(str1)
    
n = (len(list1))
i = 0
while i<n:
    count = list1.count(list1[i])
    dict1[list1[i]] = count
    i += 1

print("Input : ",list1)
print("Output : ",dict1)


