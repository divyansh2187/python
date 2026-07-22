arr = [1,5,5,5,6,7,]




# ---------most optimal solution----------------


# def func(arr,t):
#     def lower_bound(arr,t):
#         low = 0
#         high= len(arr)-1
#         lower = -1
#         while low<=high:
#             mid = (low + high)//2
#             if arr[mid] >= t:
#                 high = mid-1
#                 lower = mid
#             else:
#                 low = mid+1
#         return lower
    
#     def higher_bound(arr,t):
#         low = 0
#         high= len(arr)-1
#         upper = -1
#         while low<=high:
#             mid = (low + high)//2
#             if arr[mid] > t:
#                 high = mid-1
#                 upper = mid
#             else:
#                 low = mid+1
#         return upper
    
#     def output(arr,t):
#         lower = lower_bound(arr,t)
#         if lower == -1 or arr[lower] != t:
#             return [-1,-1]
#         upper = higher_bound(arr,t)

#         if upper == -1:
#             upper = len(arr)
#         return[ lower , upper-1]
    
#     return output(arr,t)






# --------------my solution-------------------

# def func(arr,t):
#     low = 0
#     high = len(arr)-1
#     lower = -1
#     upp = -1
#     while low<=high:
#         mid = (low+high)//2
#         if t < arr[mid]:
#             high = mid-1
#         elif t> arr[mid]:
#             low = mid+1
#         else:
#             lower = mid
#             upp = mid
#             while lower > 0 and arr[lower-1] == t:
#                 lower-=1
#             while upp < len(arr)-1 and arr[upp+1] == t:
#                 upp+=1

#             break
       
#     return [lower,upp]

        



# -------------brute force ------------------


# def func(arr,t):
#     first = -1
#     last = -1
#     for i in range(len(arr)):
#             if arr[i] == t and first == -1:
#                 first = i
#             elif arr[i] == t:
#                 last = i
#     return [first,last]

                 

       


print(func(arr,5))    