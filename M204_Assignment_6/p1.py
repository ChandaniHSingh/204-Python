'''
Q.1. Write a Menu Driven (Menu: PUSH, POP, PEEP, PRINT, EXIT) program in Python to
implement stack operations on a stack of integers using a class consisting of attributes
Stack (a List consisting of elements of the Stack) and TOP, and methods PUSH, POP,
PEEP and PRINT.
'''

class Stack :
    def __init__(self):
        self.lst = []

    def is_empty(self):
        return self.lst == []
    
    def push(self,val):
        self.lst.append(val)
        
    def pop(self):
        return self.lst.pop()

    def peep(self):
        print(self.lst[len(self.lst) - 1])
        
    def print(self):
        print(self.lst)



s1 = Stack()
while True:
    print("-------Operation-------")
    print("1 Push")
    print("2 Pop")
    print("3 Peep")
    print("4 Print")
    print("5 Exit")
    op = input("Select Option : ")
    try:
        op = int(op)
    except:
        print("Please enter Numbers only ")
        continue

    if(op == 1):
        s1.push(int(input("Enter Value : ")));
    elif(op == 2):
        if(s1.is_empty()):
            print("Stack is EMpty...")
        else:
            s1.pop()
    elif(op == 3):
        if(s1.is_empty()):
            print("Stack is EMpty...")
        else:
            s1.peep()
    elif(op == 4):
        if(s1.is_empty()):
            print("Stack is EMpty...")
        else:
            s1.print()
    elif(op == 5):
        print("Thank You using STack Program")
        break
    else:
        print("Please Enter Valid Selection....")
        
        
