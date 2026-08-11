
# DSA in Python - Combination Sum II | Recursion & Backtracking | Leetcode 40 - Part 76
# ---------brute force approach----------

# def combinationSum(n,t):

#     def recursion(idx,total,subset,n,result,t):
#         if total == t:
#             return result.add(tuple(sorted(subset.copy())))
#         if total > t:
#             return
#         if idx >= len(n):
#             return

#         subset.append(n[idx])
#         recursion(idx+1,total+n[idx],subset,n,result,t)
#         subset.pop()

#         recursion(idx+1,total,subset,n,result,t)


#     result = set()
#     subset = []

#     recursion(0,0,subset,n,result,t)
#     return list(result)
# n= [1,1,2,1,2]
# print(combinationSum(n,4))



# ----------optimal approach ----------------

def combinationSum(num,t):

    def recursion(idx , total , subset ,result,num):
        if total == 0:
            return result.append(subset.copy())

        if total < 0:
            return
        
        for i in range(idx,len(num)): 
            if i>idx and num[i] == num[i-1]:
                continue
            subset.append(num[i])
            recursion(i+1,total-num[i],subset, result,num)
            subset.pop()

    result = []
    subset = []
    num.sort()
    recursion(0,t,subset,result,num)

    return result
print(combinationSum([1,1,2,1,2],4))


