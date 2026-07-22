arr = [4,5,6,7,0,1,2]

def func(arr):
    low = 0 
    high = len(arr)-1
    smallest = float('inf')
    while low<=high:
        mid = (low+high)//2
        if arr[low]<=arr[mid]:
               smallest = min(smallest, arr[low])
               low = mid+1
        else:
               smallest= min(smallest, arr[mid])
               high = mid-1
    return smallest



print(func(arr))


        