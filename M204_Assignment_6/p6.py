'''
Q.6. Write a Python program to demonstrate multi-level, multiple inheritance and MRO.
'''

class Department:
    def __init__(self,dname,address):
        self.dname = dname
        self.address = address
    def dispDept(self):
        print("Department Name : ",self.dname)
        print("Address : ",self.address)

class Course1(Department):
    def __init__(self,c1name,c1year,dname,address):
        Department.__init__(self,dname,address)
        self.c1name = c1name
        self.c1year = c1year
    def dispCourse1(self):
        print("Course Name : ",self.c1name)
        print("Course Year : ",self.c1year)

class Course2(Department):
    def __init__(self,c2name,c2year,dname,address):
        Department.__init__(self,dname,address)
        self.c2name = c2name
        self.c2year = c2year
    def dispCourse2(self):
        print("Course Name : ",self.c2name)
        print("Course Year : ",self.c2year)

class Exam(Course1,Course2):
    def __init__(self,examdate,c1name,c1year,c2name,c2year,dname,address):
        Course1.__init__(self,c1name,c1year,dname,address)
        Course2.__init__(self,c2name,c2year,dname,address)
        self.examdate = examdate
    def dispExam(self):
        self.dispDept()
        self.dispCourse1()
        self.dispCourse2()
        print("Exam Date : ",self.examdate)


e = Exam("16-06-2022","MCA","2","PGDCA","1","DCS-VNSGU","Surat,Gujarat,India")
e.dispExam()

        
