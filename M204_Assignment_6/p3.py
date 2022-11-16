'''
Q.3. Write a Python program to do the following:
 Define a class myDate consisting of attributes day, month and year and following
methods:
o addDays(myDate, int) where the 1st argument is a myDate class type and 2nd
argument is an integer type with default value as 0. The method should
add/subtract int days (depending on the integer i.e. add if positive and
subtract if negative) to/from the myDate and return new date of myDate type.
o formatDate(myDate, formatString) where the 1st argument is a myDate class
type and 2nd argument is a format string of string type. The method will return
the date in the given format. Consider only the following format strings in
this program. ‘dd-mm-yyyy’, ‘mm-dd-yyyy’ and ‘yyyy-mm-dd’.
 Implement the above
'''

import datetime as dt

class myDate:
    def __init__(self,day,month,year):
        self.date = dt.datetime(year,month,day)

    def addDays(self,d):
        self.date = self.date + dt.timedelta(days=d)     
        return self

    def formatDate(self,fs):
        if(fs == "dd-mm-yyyy"):
            return self.date.strftime("%d-%m-%Y")
        elif(fs == "mm-dd-yyyy"):
            return self.date.strftime("%m-%d-%Y")
        elif(fs == "yyyy-mm-dd"):
            return self.date.strftime("%Y-%m-%d")
        else:
            return self.date.strftime("%d-%m-%Y")


d = int(input("Date Day : "))
m = int(input("Date Month : "))
y = int(input("Date Year : "))

md = myDate(d,m,y)

while True:
    print("----Menu------")
    print("1 addDays")
    print("2 formatDate")
    print("3 Exit")

    op = int(input("ENter operation : "))

    if(op == 1):
        md.addDays(int(input("ENter Days : ")))
    elif(op == 2):
        print("----Menu for FormatDate------")
        print("1 dd-mm-yyyy")
        print("2 mm-dd-yyyy")
        print("3 yyyy-mm-dd")

        fdop = int(input("Select FormatDate type : "))
        if(fdop == 1):
            print("Date : ",md.formatDate("dd-mm-yyyy"))
        elif(fdop == 2):
            print("Date : ",md.formatDate("mm-dd-yyyy"))
        elif(fdop == 3):
            print("Date : ",md.formatDate("yyyy-mm-dd"))
        else:
            print("Date : ",md.formatDate("dd-mm-yyyy"))

    elif(op == 3):
        print("Thank You for using myDate Class....")
        break

    else:
        print("Please enter valid Choice ....")
            
            
        
