arr = [1,2,3,4,5,1,7,8]


# ----------------way one-----------------
# def funcc(arr):
#     shorted = False
#     for i in range(1, len(arr)-1):
#         if arr[i] > arr[i-1] and arr[i] < arr[i+1]:
#             shorted = True
#         else:
#             shorted = False
#             break
#     return shorted
    
# print(funcc(arr))






# ----------------way two-----------------
# def funcc(arr):
#     for i in range(0, len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#     return True

# print(funcc(arr))