'''
Q.4. Write a Python program to create a file of elements of any data type (mixed data type, i.e. some elements maybe of type int, some elements of type float and some elements of type string). Split this file into three file containing elements of same data type (i.e. 1st file of integers only, 2nd file of float only and 3rd file of strings only). Take input from the user to create the file.
'''

design = 50*"="
f = open("file4.txt","w")
print("enter END to STOP...")
print("Enter Any Input : ")
while True:
    txt = input()
    if txt.upper() == 'END':
        break
    f.write(txt+'\n')
f.close()

f = open("file4.txt")
fInt = open("fileInt.txt","w")
fFloat= open("fileFloat.txt","w")
fStr= open("fileStr.txt","w")
for i in f.readlines():
    for j in i.strip().split(" "):
        try:
            num = int(j)
            fInt.write(j+"\n")
        except:  
            try:
                num = float(j)
                fFloat.write(j+"\n")
            except:
                num = str(j)
                fStr.write(j+"\n")

fInt.close()
fFloat.close()
fStr.close()
f.close()

print(design)
print("Printing Output from fileInt.txt : ")
f = open("fileInt.txt")
print(f.read())
f.close()
print(design)

print("Printing Output from fileFloat.txt : ")
f = open("fileFloat.txt")
print(f.read())
f.close()
print(design)

print("Printing Output from fileStr.txt : ")
f = open("fileStr.txt")
print(f.read())
f.close()
print(design)               

