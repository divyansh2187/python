

# DSA in Python - Combination Sum III | Recursion & Backtracking | Leetcode 216 - Part 78


# -------my solution----------------------------

# def Combination(n,t):

#     def recursion(idx , total , result , subset , n , t,num):

#         if len(subset) == n:
#             if total == t:
#                 return result.append(subset.copy())
#             return

#         if total > t:
#             return

#         if idx >= len(num):
#             return

#         subset.append(num[idx])
#         recursion(idx+1 , total+num[idx] , result , subset , n , t , num)
#         subset.pop()

#         recursion(idx+1 , total , result , subset , n , t , num)

#     num = [1,2,3,4,5,6,7,8,9]
#     subset = []
#     result = []
#     recursion(0 , 0 , result ,subset , n , t, num )
#     return result

# print(Combination(4,13))

   
# ----------optimal solution ---------------------

def combinationSum(n,t):

    def recursion(idx , total , result , subset ,  n , t , num):

        if len(subset) == n:
            if total == t:
                result.append(subset.copy())
            return

        if total > t:
            return 

        for i in range(idx , len(num)):
            subset.append(num[i])
            recursion(i+1 , total+num[i] , result , subset , n , t , num)
            subset.pop()

    result = []
    num = [1,2,3,4,5,6,7,8,9]
    subset = []
    recursion(0,0,result , subset , n , t , num)
    return result

print(combinationSum(4,13))