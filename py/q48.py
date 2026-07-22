arr = [ 1,1,2,2,3,3,4,4,5,5]



def func(arr,t):
    low = 0
    high = len(arr)-1
    lowerBound = len(arr)
    while low <= high:
        mid = (low + high)//2
        if t <= arr[mid]:
            high = mid-1
            lowerBound = arr[mid]
        else:
            low = mid+1
    return lowerBound

print(func(arr,1))


            
