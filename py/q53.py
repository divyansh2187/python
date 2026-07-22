arr = [2,4,6,8,10,12,14,16,18,20]

def func(arr,t):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == t:
            return mid
        if arr[mid] <= arr[high]:
            if arr[mid]<= t <= arr[high]:
                low= mid+1
            else:
                high = mid-1
        else:
            if arr[low] <= t <= arr[mid]:
                high = mid-1
            else:
                low = mid+1
    return -1

print(func(arr,10))










# ---------brute force--------
# def func(arr,t):
#     for i in range(len(arr)):
#         if arr[i] == t:
#             return i
#     return -1

# print(func(arr,100))