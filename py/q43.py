matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def func(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row-1):
        for j in range(i+1,col):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(row):
        matrix[i].reverse()

func(matrix)
print(matrix)
            




# ---------------------------brute force----------------------

# def func(matrix):
#    row = len(matrix)
#    col = len(matrix[0])
#    clone = [[0 for j in range(col)] for i in range(row)]

#    for i in range(row):
#         for j in range(col):
#             clone[j][(row-1)-i] = matrix[i][j]
#    print(clone)

# func(matrix)
            