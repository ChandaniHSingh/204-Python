'''
Q.9. Write a Python program to read 2 matrices and find the following, if it is possible to do so:

1) Find sum of both the matrices.
2) Find difference of both the matrices.
3) Find product of both the matrices.
Display all the values with appropriate titles.
'''

def sum(mat1,mat2,row,col):
    mat3 = []
    for i in range(row):
        temp = []
        for j in range(col):
            x = mat1[i][j] + mat2[i][j]
            temp.append(x)
        mat3.append(temp)
        temp = []
    return mat3

def diff(mat1,mat2,row,col):
    mat3 = []
    for i in range(row):
        temp = []
        for j in range(col):
            x = mat1[i][j] - mat2[i][j]
            temp.append(x)
        mat3.append(temp)
        temp = []
    return mat3
def pro(mat1,mat2,n1,m1,n2,m2):
    mat3 = []
    for i in range(n1):
        temp = []
        for j in range(m2):
            x = 0
            for k in range(m1):
                x += mat1[i][k] * mat2[k][j]
            temp.append(x)
        mat3.append(temp)
        temp = []
    return mat3

def takeMatrix(n,m):
    mat = []
    for i in range(n):
        temp=[]
        for j in range(m):
            x=int(input('Enter number : '))
            temp.append(x)
        mat.append(temp)
        temp = []
    return mat

print("Enter Rows and Columns for 1st Matrix : ")
n1=int(input('Enter no. of Rows : '))
m1=int(input('Enter no. of Columns : '))
mat1=takeMatrix(n1,m1)
print(mat1)
print("Enter Rows and Columns for 2nd Matrix : ")
n2=int(input('Enter no. of Rows : '))
m2=int(input('Enter no. of Columns : '))
mat2=takeMatrix(n2,m2)
print(mat2)

if ((n1 == n2) and (m1 == m2)):
    sumMat = sum(mat1,mat2,n1,m1)
    print("Sum of Matrix : ",sumMat)
    diffMat = diff(mat1,mat2,n1,m1)
    print("Difference of Matrix : ",diffMat)
else:
    print("Sum and Difference is Not possible..")

if (m1 == n2):
    proMat = pro(mat1,mat2,n1,m1,n2,m2)
    print("Product of Matrix : ",proMat)
else:
    print("Product is Not possible..")
            
