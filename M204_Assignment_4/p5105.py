'''
Q.5. Write a Python program to create a file containing student records where each record contain rollno and marks in 3 subjects separated by a comma (marks to be considered as list of 3 values). e.g. records of students: 1, [45, 40, 35], 2, [41, 38, 39], 3, [35, 30, 37] (each line of the file containing record of only 1 student). Prepare mark list in the following format:
Roll No. Mark-1 Mark-2 Mark-3 Total
1 45 40 35 120
'''

design = 50*"="
f = open("file5.txt","w")
print("enter END to STOP...")
print("Enter input per line like : rollno [m1,m2,m3]")
print("Enter Any Input : ")
while True:
    txt = input()
    if txt.upper() == 'END':
        break
    f.write(txt+'\n')
f.close()

f = open("file5.txt")
print("Roll No. Mark-1 Mark-2 Mark-3 Total")
for i in f.readlines():
    record = i.split(" ")
    print(record[0],end="\t")
    ans = str(record[1])
    ans = ans[1:len(ans)-2]
    marks = ans.strip().split(",");
    sum = 0
    for m in marks:
        print(m,end = "\t")
        sum += int(m)
    print(sum)
f.close()

