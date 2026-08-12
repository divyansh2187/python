

# DSA in Python - Subset Sums | Recursion & Backtracking | GFG Problem - Part 77

def sumsequence(n):

    def recursion(idx , result , total ):

        if idx >= len(n):
            return result.append(total)

        sum = total + n[idx]
        recursion(idx+1 , result , sum )


        recursion(idx+1 , result , total)

    result = []
    recursion(0,result , 0)
    return result 
n = [1,3,5]
print(sumsequence(n))


        
