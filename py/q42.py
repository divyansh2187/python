# matrix = [[1, 2, 3], [4, 5, 0], [7, 8, 9]]

# ---------------optimized-----------------
# def funcc(matrix):
#     row = len(matrix)
#     colum = len(matrix[0])

#     rowTrack  =[0 for i in range(row)]
#     colTrack  =[0 for i in range(colum)]

#     for i in range(row):
#         for j in range(colum):
#             if matrix[i][j]==0:
#                 rowTrack[i] = -1
#                 colTrack[j] = -1

#     for i in range(row):
#         for j in range(colum):
#             if rowTrack[i] == -1 or colTrack[j] ==-1:
#                 matrix[i][j]=0
# funcc(matrix)
# print(matrix)



# -----------------brute force-----------------
# def MarkInfinity(matrix, i ,j):
#     row = len(matrix)
#     colum = len(matrix[0])

#     for c in range(colum):
#        if matrix[i][c] != 0:
#            matrix[i][c] = float('inf')
#     for r in range(row):
#          if matrix[r][j] != 0:
#            matrix[r][j] = float('inf')
#     return
        
           

# def funcc(matrix):
#     row = len(matrix)
#     colum = len(matrix[0])

#     for i in range(row):
#         for j in range(colum):
#             if matrix[i][j] == 0:
#                 MarkInfinity(matrix , i , j)
#     for i in range(row):
#         for j in range(colum):
#             if matrix[i][j] == float('inf'):
#                  matrix[i][j] = 0
#     return

# funcc(matrix)
# print(matrix)

    




