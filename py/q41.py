matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row = len(matrix)
colum = len(matrix[0])
arr = [[0] * colum for i in range(colum)]

for i in range(row):
    for j in range(colum):
        arr[j][i] = matrix[i][j]

print(matrix)
print(arr)