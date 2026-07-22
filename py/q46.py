nums = [1,0,-1,0,-2,2]



# -------------optimal approach tc n2 ---------------

def forSum(arr , tar):
    n = len(arr)
    arr.sort()
    result = []


    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            k= j+1
            l=n-1

            while k < l:
                total = arr[i]+arr[j]+arr[k]+arr[l]
                if total == tar:
                    result.append([arr[i],arr[j],arr[k],arr[l]])
                    k+=1
                    l-=1

                    while k<l and arr[k] == arr[k-1]:
                        k+=1
                    while k<l and arr[l] == arr[l+1]:
                        l-=1
                elif total > tar:
                    l-=1 
                else:
                    k+=1
                
    return [list(x) for x in result]
print(forSum(nums , 0))
                    
                        



          
        



# ------------brute force tc n3-------------
# def forSum(num):
#     n = len(num)
#     result = set()

#     for i in range(n):
#         for j in range(i+1,n):
#             map = set()
#             for k in range(j+1,n):
#                 numb = -(num[i]+num[j]+num[k])
#                 if numb in map:
#                     result.add(tuple(sorted([num[i],num[j],num[k],numb])))
#                 map.add(num[k])
#     return [list(x) for x in result]
# print(forSum(nums))






# -------------brute force tc n4-------------
# def forsum(num):
#     n = len(num)
#     result = set()
#     for i in range(0,n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for t in range(k+1,n):
#                     if num[i]+num[j]+num[k]+num[t]==0:
#                         result.add(tuple(sorted([num[i],num[j],num[k],num[t]])))
#     return [list(x) for x in result]

# print(forsum(nums))
