'''
Q.7. Write a Python program to create a text file of multiple lines. Take input of a word from the user and then display all the lines from the file containing this word along with the frequency of the word in that line.
'''

design = 50*"="
print("Enter Lines : ")
f = open("file7.txt","w")
while True:
    txt = input()
    if txt.upper() == "END":
        break
    f.write(txt+"\n")

f.close()

print(design)
word = input("Enter word to find : ")
print(design)

print("count   Line")
print(design)
with open("file7.txt") as f:
    for line in f:
        count = 0
        count = line.count(word)
        if count > 0:
            print(count,end='\t')
            print(line.strip())
