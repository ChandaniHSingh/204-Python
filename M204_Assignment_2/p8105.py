'''
Q.8. Write a Python program to read a m X n matrix and find the following:

1) Find sum of each row and each column.
2) Find the highest and lowest from each row, each column, and the whole matrix.
3) Find the sum of its diagonal elements if the matrix is a square matrix.
4) Find the transpose of the matrix.
Display all the values with appropriate titles.
'''

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

def showMatrix(mat,n,m):
    for i in range(n):
        for j in range(m):
            print(mat[i][j],end = " ")
        print("\n")
    
def sumRowWise(mat,n,m):
    for i in range(n):
        sum =0
        for j in range(m):
            sum += mat[i][j]
        print("Sum of ",i+1,"th Row : ",sum)

def sumColWise(mat,n,m):
    for i in range(m):
        sum =0
        for j in range(n):
            sum += mat[j][i]
        print("Sum of ",i+1,"th Column : ",sum)

def maxRowWise(mat,n,m):
    k = 0
    for i in mat:
        print("Max of Row-",k+1," : ",max(i))
        k += 1

def maxColWise(mat,n,m):
    for i in range(m):
        max = mat[0][i]
        for j in range(n):
            if(mat[j][i] > max):
                max = mat[j][i]
        print("Max of Column-",i+1," : ",max)

def minRowWise(mat,n,m):
    k = 0
    for i in mat:
        print("Min of Row-",k+1," : ",min(i))
        k += 1

def minColWise(mat,n,m):
    for i in range(m):
        min = mat[0][i]
        for j in range(n):
            if(mat[j][i] < min):
                min = mat[j][i]
        print("Min of Column-",i+1," : ",min)               
 

def maxMat(mat):
    row = max(mat)
    print("Max of Whole Matrix  : ",max(row))

def minMat(mat):
    row = min(mat)
    print("Max of Whole Matrix  : ",min(row))

def isSquare(mat,n,m):
    if(n== m):
        return True
    else:
        return False

def diagonalSum(mat,n,m):
    sum1 = 0
    sum2 = 0
    if(isSquare(mat,n,m)):
        for i in range(n):
            for j in range(m):
                if(i==j):
                    sum1 += mat[i][j]
                if(i+j == n-1):
                    sum2 += mat[i][j]
        print("Matrix is Square")
        print("1st Diagonal Sum : ",sum1)
        print("2nd Diagonal Sum : ",sum2)
    else:
        print("Matrix is Not Square")
                    
        

def transposeMat(oldMat,n,m):
    mat = []
    for i in range(m):
        temp=[]
        for j in range(n):
            temp.append(oldMat[j][i])
        mat.append(temp)
        temp = []
    showMatrix(mat,m,n)
    
print("Enter Rows and Columns for 1st Matrix : ")
n=int(input('Enter no. of Rows : '))
m=int(input('Enter no. of Columns : '))
mat=takeMatrix(n,m)
print(mat)
showMatrix(mat,n,m)
sumRowWise(mat,n,m)
sumColWise(mat,n,m)
maxRowWise(mat,n,m)
maxColWise(mat,n,m)
minRowWise(mat,n,m)
minColWise(mat,n,m)
maxMat(mat)
minMat(mat)
diagonalSum(mat,n,m)
transposeMat(mat,n,m)


