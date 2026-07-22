arr = [1,3,4,7,8,9]

def func(arr,t):
    low = 0
    high = len(arr)-1
    index = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= t:
            high = mid-1
            index = mid
        else:
            low = mid+1
    return index

print(func(arr,3))


