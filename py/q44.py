matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

def spiral(matrix):
    row = len(matrix)
    col = len(matrix[0])
    t,l = 0,0
    b,r=row-1,col-1
    result = []

    while t <= b and l <= r:
        for i in range(l,r+1):
            result.append(matrix[t][i])
        t+=1
        for i in range(t,b+1):
             result.append(matrix[i][r])
        r-=1

        if t <= b:
            for i in range(r , l-1,-1 ):
                result.append(matrix[b][i])
            b-=1

        if l <= r:
            for i in range(b,t-1,-1):
                result.append(matrix[i][l])
            l+=1
    return result
print(spiral(matrix))

        



