arr = [-2,1,-3,4,-1,2,1,-5,4]


def funcc(arr):
    n = len(arr)
    maxi = float('-inf')
    total= 0
    for i in arr:
        total = i+total
        maxi =max(maxi, total)
        if total < 0:
            total = 0
    return maxi
print(funcc(arr))
             





# -----------brute force ---------------
# def funcc(arr , i=0):
#   maximum = float('-inf')
#   for i in range(0, len(arr)):
#       total = 0
#       for j in range(i,len(arr)):
#          total += arr[j]
#          maximum = max(total,maximum)
#   return maximum



# print(funcc(arr))