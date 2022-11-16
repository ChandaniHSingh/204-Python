'''
Q.2. Write a Python program to create two text files containing different words. Create a list
containing words that exist in both the files.
'''

#file 1
f = open("p2f1.txt","w")
while True:
    text = input()
    if text.upper() == "END":
        break
    f.write(text.strip()+" ")
f.close()

f = open("p2f1.txt","r")
print(f.read())
f.close()


#file 2

f = open("p2f2.txt","w")
while True:
    text = input()
    if text.upper() == "END":
        break
    f.write(text.strip()+" ")
f.close()

f = open("p2f2.txt","r")
print(f.read())
f.close()


# read from file and convert to list

f = open("p2f1.txt","r")
str1 = f.read().strip()
lst1 = str1.split(" ")
print(lst1)
f.close()

f = open("p2f2.txt","r")
str2 = f.read().strip()
lst2 = str2.split(" ")
print(lst2)
f.close()


#convert to set to intersection

set1 = set(lst1)
set2 = set(lst2)

set3 = set1.intersection(set2)
lst3 = list(set3)

print(lst3)
