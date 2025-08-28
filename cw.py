matrix=[[1,2,3],[4,5,6],[7,8,9]]

print (matrix)

print(len(matrix[0]))

print(matrix[1][2])

rows=len(matrix)
columns=len(matrix[0])
for i in range(0,rows):
    for j in range(0,columns):
        print(matrix[i][j],end=" ")
    print("\n")

r=int(input("Enter the nuber of rows: "))
c=int(input("Enter the nuber of columns: "))

m=[]

for i in range(r):
    temp=[]
    for j in range(c):
        x=int(input("Enter your element: "))
        temp.append(x)
        m.append(temp)

        