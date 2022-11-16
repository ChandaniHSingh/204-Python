'''
Q.1. Write a Python program to create a file of numbers by taking input from the user and then display the content of the file. You can take input of non-zero numbers, with an appropriate prompt, from the user until the user enters a zero to create the file assuming that the numbers are non-zero.
'''

f = open("file1.txt","w")
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
print("Printing Output from file1.txt : ")
f = open("file1.txt")
print(f.read())
f.close()

          
