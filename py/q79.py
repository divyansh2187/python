# Combination Sum | Recursion & Backtracking | Leetcode 39 - Part 75 [Hindi]

def combination(n,t):

    subset = []
    result = []

    def recursion(idx,total, subset):
        if total > t:
            return

        if total == t:
            return result.append(subset.copy())
        if idx >= len(n):
            return

        subset.append(n[idx])
        recursion(idx, total+n[idx] , subset )
        subset.pop()
        


        recursion(idx+1,total, subset )
        

    recursion(0,0,subset)

    return result
n = [2,3,4,7]
print(combination(n , 7))



    


            


     