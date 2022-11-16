'''
Q.2. Write a Python program to create a text file of multiple lines. Display the following:
1. Entire text file
2. 1st n lines of the text file.
3. m lines starting from the nth line
4. number of words in each line
'''

design = 50*"="
f = open("file2.txt","w")
print("Enter END to Stop : \n")
print("Enter Input: \n")

while True:
    txt = input()
    if txt.upper() == 'END':
        break
    f.write(txt+'\n')    
f.close()
print(design)

f = open("file2.txt")

print("1. Entire text file : \n\n")

print(f.read().strip())

print(design)

print("2. 1st N lines of the text file. : ")

n = int(input("Enter N : "))
f.seek(0,0)
for i in range(n):
    print(f.readline().strip())

print(design)

print("3. M lines starting from the Nth line : ")

m = int(input("Enter M : "))
for i in range(m):
    print(f.readline().strip())
    
print(design)  
f.close()

print("4. number of words in each line : ")

f = open("file2.txt")
for i in f.readlines():
    count = i.count(" ")
    print(count+1,"words")
    
print(design) 
f.close()   

      

