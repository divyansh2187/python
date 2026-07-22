# SA in Python - Advanced Recursion | Generate Subsequences with Sum K | Backtracking - Part 70


result= []
sum = 0
num = [5,9,4]
k =9


def sumofseq(index,sum,subset):
    if sum == k:
        return result.append(subset.copy())
    if sum > k:
        return
    if index >= len(num):
        return
    
    subset.append(num[index])
    sum += num[index]
    sumofseq(index+1, sum , subset)
    e=subset.pop()
    sum-=e
    sumofseq(index+1, sum , subset)


sumofseq(0,0,[])
print(result)

    



    

