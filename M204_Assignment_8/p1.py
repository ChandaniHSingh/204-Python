'''
Q.1. Write a Python program to create a text file of multiple lines. Display the following:
1. Line number and number of words in each line.
2. Display each line with the words in backward order.
3. Display line numbers of the empty lines.
4. Display all the lines that contain alphabets and digits both.
5. Display all the lines that contain only alphabets.
'''

# write to file

f = open("p1f1.txt","a")

while True:
    text = input()
    if text.upper() == "END":
        break
    f.write(text.strip()+"\n")

f.close()

# read from file

f = open("p1f1.txt","r")
for i in f:
    print(i.strip())

# line number and number of words
print("Line number and number of words in each line.\n")
f = open("p1f1.txt","r")
count = 0

print("count  No.of Word")
for i in f:
    count += 1
    if(len(i.strip()) == 0):
        print(count,"     ",0)
    else:
        print(count,"     ",len(i.strip().split(" ")))

# Display each line with the words in backward order.
print("Display each line with the words in backward order.\n")
f = open("p1f1.txt","r")
count = 0

print("count  No.of Word")
for i in f:
    line = i.strip()
    line = line.split(" ")
    line = line[::-1]
    for word in line:
        print(word,end=" ")
    print()


#Display line numbers of the empty lines.
print("Display line numbers of the empty lines.\n")
f = open("p1f1.txt","r")
count = 0

for i in f:
    count += 1
    if(len(i.strip()) == 0):
        print(count)

#Display all the lines that contain alphabets and digits both.
print("Display all the lines that contain alphabets and digits both.\n")
f = open("p1f1.txt","r")
count = 0

for i in f:
    lst = i.strip().split(" ")
    if any(k.isalpha() for k in lst) and any(k.isdigit() for k in lst):
        print(i.strip())

#Display all the lines that contain only alphabets.
print("Display all the lines that contain only alphabets.\n")
f = open("p1f1.txt","r")
count = 0

for i in f:
    lst = i.strip().split(" ")
    if all(k.isalpha() for k in lst):
        print(i.strip())
