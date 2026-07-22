arr = [1,99,101,98,2,5,3,100,1]

# ---------optimal solution----------------------
def func(arr):
    arr = set(arr)
    count = 0
    maxCount = 0
    for i in arr:
        if i-1 not in arr:
            num = i
            count = 1
            while num+1 in arr:
                count+=1
                num +=1
            maxCount = max(maxCount,count)
        
    return maxCount

print(func(arr))












# -------------- more good solution----------------------
# def func(arr):
#     arr.sort()
#     last_smallest = float('-inf')
#     count = 0
#     maxCount = 0
#     for i in range(len(arr)):
#         if arr[i]-1 == last_smallest:
#             count +=1
#             last_smallest = arr[i]
#         elif arr[i] != last_smallest:
#             last_smallest = arr[i]
#             count=1
#         maxCount = max(maxCount,count)
#     return maxCount

# print(func(arr))





# ----------------my solution----------------------
# def func(arr):
#     arr.sort()
#     maxc = 0
#     count = 1
#     for i in range(len(arr)-1):
#         if arr[i+1] == arr[i]+1:
#             count+=1
#         else:
#             maxc = max(maxc,count)
#             count = 1
#     maxc = max(maxc,count)
#     return maxc
            
# print(func(arr))




# -------------brute force solution------------------------------
# def func(arr):
#     maxCOUNT = 0

#     for i in range(len(arr)):
#         num = arr[i]
#         count = 1
#         while num+1 in arr:
#             count+=1
#             num = num+1
#         maxCOUNT = max(maxCOUNT,count)
#     return maxCOUNT
    
       

   



