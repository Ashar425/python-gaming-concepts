matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Matrix:", matrix)
print("Number of columns:", len(matrix[0]))
print("Element at [1][2]:", matrix[1][2])

rows = len(matrix)
columns = len(matrix[0])

print("\nPrinting matrix elements:")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()

r = int(input("\nEnter the number of rows: "))
c = int(input("Enter the number of columns: "))

m = []
for i in range(r):
    temp = []
    for j in range(c):
        x = int(input(f"Enter element at [{i}][{j}]: "))
        temp.append(x)
    m.append(temp)

print("\nYour entered matrix:")
for i in range(r):
    for j in range(c):
        print(m[i][j], end=" ")
    print()

ro = int(input("\nEnter the number of rows (square matrix): "))
col = ro

ma = []
for i in range(ro):
    temp = []
    for j in range(col):
        x = int(input(f"Enter element at [{i}][{j}]: "))
        temp.append(x)
    ma.append(temp)

print("\nSecond user matrix:")
for i in range(ro):
    for j in range(col):
        print(ma[i][j], end=" ")
    print()

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

add = [[0, 0], [0, 0]]
sub = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        add[i][j] = matrix1[i][j] + matrix2[i][j]
        sub[i][j] = matrix1[i][j] - matrix2[i][j]

print("\nMatrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Addition:", add)
print("Subtraction:", sub)