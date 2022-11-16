'''
Q.2. Write a Menu Driven (Menu: INSERT, DELETE, PRINT, EXIT) program in Python to
implement Simple Queue Operations on a simple queue of integers using a class
consisting of attributes SQueue (a List consisting of elements of the Simple Queue),
Front and Rear and methods INSERT, DELETE and PRINT.
'''

class Queue:
    def __init__(self):
        self.lst = []

    def insert(self,val):
        self.lst.append(val)

    def is_empty(self):
        if(len(self.lst) == 0):
            return True
        else:
            return False

    def delete(self):
        del(self.lst[0])

    def print(self):
        print(self.lst)


q1 = Queue()

while True:
    print("----Menu-----")
    print("1 Insert")
    print("2 Delete")
    print("3 Print")
    print("4 Exit")

    op = input("Select Menu : ")
    try:
        op = int(op)
    except:
        print("Please enter numbers only ")
        continue

    if(op == 1):
        q1.insert(int(input("ENter Value : ")))

    elif(op == 2):
        if(q1.is_empty() == False):
            q1.delete()
        else:
            print("Queue is EMpty...")

    elif(op == 3):
        if(q1.is_empty() == False):
            q1.print()
        else:
            print("Queue is EMpty...")

    elif(op == 4):
        print("Thank You for using Queue Program....")
        break

    else:
        print("Please enter valid Selection....")
        
    
