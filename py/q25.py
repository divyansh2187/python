
arr = [7,3,6,8,4,2,6,7,90,5,4,5,6,4,1,2]


def funcc(arr1 , arr2):
    result = []
    n , m = len(arr1) ,len(arr2)
    i, j = 0 , 0 

    while i<n and j<m:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i < n:
        while i < n:
            result.append(arr1[i])
            i += 1
    if j < m:
        while j < m:
            result.append(arr2[j])
            j += 1
    return result


def mergeShort(arr):
    if len(arr ) == 1:
        return arr
    mid = len(arr)//2
    leftA = arr[ :mid]
    rightA = arr[mid: ]
    left = mergeShort(leftA)
    right = mergeShort(rightA)
    return funcc(left , right)

print(mergeShort(arr))
     
        