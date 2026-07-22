arr = [-1,0,1,2,-1,-4]

# ----------optmal approch ---------------
def func(arr):
    arr.sort()
    result = []
    n= len(arr)

    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        else:
            j = i+1
            k = n-1
            while j < k:
                total = arr[i]+arr[j]+arr[k]
                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    result.append([arr[i],arr[j],arr[k]])
                    j+=1
                    k-=1
                    while j < k and arr[j] == arr[j-1]:
                        j+=1
                    while k > j and arr[k] == arr[k+1]:
                        k-=1
    return result
print(func(arr))





# # ----------brute force tc n2 ---------------
# def func(arr):
#     n = len(arr)
#     result = set()
    

#     for i in range(n):
#         map = set()
#         for j in range(i+1,n):
#             num = -(arr[i]+arr[j])
#             if num in map:
#                 triplet = tuple(sorted([arr[i],arr[j],num]))
#                 result.add(triplet)
#             else:
#                 map.add(arr[j])
#     return result
# print(func(arr))


 
# ---------------brute force tc n3-------------
# def func(arr):
#     n = len(arr)
#     map = set()

#     for i in range(n):
#         j = i+1
#         while j < n:
#             k = j+1
#             while k < n:
#                 if arr[i]+arr[j]+arr[k]==0:
#                     triplet = tuple(sorted([arr[i],arr[j],arr[k]]))
#                     
# 
# 
# 
# \map.add(triplet)
#                 k+=1
#             j+=1 

#     return [list(x) for x in map]
# print(func(arr))