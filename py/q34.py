arr = [0,1,3,2,4,6]


def func(arr):
   n = len(arr)
   total1 = n*(n+2)//2
   total2 = sum(arr)
   return total1 - total2

print(func(arr))





# more good solution ========================

# def func(arr):
#     map = {}
#     for i in range(1, len(arr) + 2):
#         map[i]=0
#     for i in arr:
#         map[i] = 1
#     for key in map:
#         if map[key] == 0:
#             return key
        
# print(func(arr))






# -----------brute force approach
# def funcc(arr):
#     for i in range(1, len(arr)+2):
#         if i not in arr:
#             return i
        
# print(funcc(arr))
