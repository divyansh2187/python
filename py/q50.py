arr = [3,4,4,4,8,9,9,10,12]
def func(arr,t):
    low = 0
    high = len(arr)-1
    floor = -1
    cli = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == t:
            return[arr[mid],arr[mid]]
        elif arr[mid] > t:
            cli = arr[mid]
            high = mid-1
        else:
            floor = arr[mid]
            low = mid + 1
    return [floor , cli]


print(func(arr,5))
    

