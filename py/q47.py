arr= [2,4,6,8,10,12,14,16,18,20]

# ----------itrative solution -----------

def func(arr , target):
    n= 0
    i = len(arr)-1
    while n < i :
        mid = (n+i)//2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
             n = mid+1
        else:
            i= mid-1

print(func(arr,18))


    







# ----------recursive solution -----------
# def func(arr, target):
#     mid  = arr[len(arr)//2]
#     point = len(arr)//2
#     if mid == target:
#         return mid
#     elif mid < target:
#        return func(arr[point+1: ] , target)
#     else:
#        return func(arr[ :point] , target)
       
# print(func(arr , 18))