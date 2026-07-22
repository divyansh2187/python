arr = [8,8,8,8,8,8,8,8,4,4,5,7,8]


def func(arr,t):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == t:
            return True
        elif arr[low] == arr[mid] == arr[high]:
            low +=1
            high -=1
        else:
            if arr[mid]<=arr[high]:
                if arr[mid]<=t<=arr[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if arr[low]<=t<=arr[mid]:
                    high = mid-1
                else:
                    low = mid+1
    return False
        
print(func(arr, 4))