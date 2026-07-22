arr = [1,0,2,0,3,0,4,0,5]

# def funcc(arr):
#     n = len(arr)
#     for i in range(n):
#         if arr[i] == 0:
#             tem = arr.pop(i)
#             arr.append(tem)
# funcc(arr)
# print(arr)

# --------------optimal solution-----------------
def funcc(arr):
    n = len(arr)
    i = 0
    j = 0
    while n > j:
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
        j+=1
   
funcc(arr)        
print(arr)