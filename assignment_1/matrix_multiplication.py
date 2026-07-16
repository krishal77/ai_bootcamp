def inputMatrix(rows,cols):
    matrix=[]

    for i in range(rows):
        row=[]
        for j in range(cols):
            value= int(input(f"enter element[{i}][{j}]"))
            row.append(value)
        matrix.append(row)

    return matrix

def multiply(A,B,ra,ca,cb):
    result=[]

    for i in range(ra):
        row=[]
        for j in range(cb):
            row.append(0)
        result.append(row)


    for i in range(ra):
        for j in range(cb):
            for k in range(ca):
                result[i][j]+=A[i][k]*B[k][j]
                    
    
    return result

def display_result(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

m= int(input("enter no of rows of matrix a: "))
n= int(input("enter no of columns of matrix a: "))

print("Enter matrix a: ")
A= inputMatrix(m,n)

p=int(input("enter rows of matrix b:"))
q= int( input("enter columns of matrix b: "))

if n!=p:
    print("multiplication not possible")

else:
    print("enter matrix B: ")
    B= inputMatrix(p,q)
    c=multiply(A,B,m,n,q)

    display_result(c)