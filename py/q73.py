

# DSA in Python - Advanced Recursion | Generate All Subsequences Using Recursion - Part 69 [Hindi]


arr = [1,2,3]
result = []

def subset(sset , indx):
    if indx >= len(arr):
        return result.append(sset.copy())
    sset.append(arr[indx])
    subset(sset , indx+1)
    sset.pop()
    subset(sset , indx+1)
        
subset([], 0)
print(result)
