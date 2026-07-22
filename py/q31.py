arr = [1,2,3,4,5,1,7,8]

def reverse(arr ,low , high ):
    j = high
    i = low
    while i < j:
        arr[i],arr[j]= arr[j],arr[i]
        i+=1
        j-=1
    return arr

def funcc(arr , k):
    k = k%len(arr)
    reverse(arr , len(arr)-k, len(arr)-1 )
    reverse(arr , 0 , len(arr)-k-1)
    reverse(arr,0 , len(arr)-1)
    
    
funcc(arr, 3)
print(arr)









# -------------- optimal solution-----------------
# def funcc(arr , k):
#     n = len(arr)
#     rotation = k%n
#     arr[:] = arr[n-rotation:]+arr[ :n-rotation]


# funcc(arr , 13)
# print(arr)





# ------------impoved brute force-----------------
# def funcc(arr , k):
#     n = len(arr)
#     rotation = k%n  
#     for _ in range(0,rotation):
#         e = arr.pop()
#         arr.insert(0,e)
# funcc(arr , 2)  
# print(arr)



# ---------------brute force=================
# def funcc(arr , k):
#     r = 1
#     while r <= k:
#         tem = arr[-1]
#         for i in range(len(arr)-2,-1,-1):
#             arr[i+1] = arr[i]
#         arr[i] = tem
#         r+=1

# funcc(arr , 3)
# print(arr)