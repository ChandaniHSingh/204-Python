'''
Q.3. Write a Python program to create a file of numbers by taking input from the user. Split this file into two files where one file contains odd numbers, and the other file contains even numbers from the file. You can take input of non-zero numbers, with an appropriate prompt, from the user until the user enters a zero to create the file assuming that the numbers are non-zero.
'''

design = 50*"="
f = open("file3.txt","w")
print("enter 0 (zero) to STOP...")
print("Enter non-zero Numnbers : ")
while True:
    num = input("Enter Number : ")
    try:
        num = int(num)
        if int(num) == 0:
            break
        f.write(str(num)+"\n")
    except:
        print("Please enter numbers only..")
f.close()

f = open("file3.txt")
fEven = open("fileEven.txt","w")
fOdd= open("fileOdd.txt","w")
for i in f.readlines():
    ans = int(i)
    if(ans % 2 == 0):
        fEven.write(str(ans)+"\n")
    else:
        fOdd.write(str(ans)+"\n")

fEven.close()
fOdd.close()
f.close()


print(design)
print("Printing Output from fileOdd.txt : ")
f = open("fileOdd.txt")
print(f.read())
f.close()
print(design)

print("Printing Output from fileEven.txt : ")
f = open("fileEven.txt")
print(f.read())
f.close()
print(design)
          
