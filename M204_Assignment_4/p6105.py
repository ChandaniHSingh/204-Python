'''
Q.6. Write a Python program to create a file of strings by taking input from the user and then create a dictionary containing each string along with their frequencies. (e.g. if the file contains ‘apple’, ‘banana’, ‘fig’, ‘apple’, ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’ then the output should be {'apple': 3, 'banana': 2, 'fig': 3, 'grapes': 2}.
'''


design = 50*"="
f = open("file6.txt","w")
print("enter END to STOP...")
print("Enter Any Input : ")
while True:
    txt = input()
    if txt.upper() == 'END':
        break
    f.write(txt+"\n")
f.close()

list1 = []
f = open("file6.txt")
for i in f.readlines():
    ans = i.strip().split(" ")
    list1.extend(ans)

f.close()

dict1 = {}
n = (len(list1))
i = 0
while i<n:
    count = list1.count(list1[i])
    dict1[list1[i]] = count
    i += 1

print("Output : ",dict1)
