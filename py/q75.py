num = [1,3,5,2,6,7]
k = 9
def check(index, sum, subset):
    if sum == k:
        return True
    
    if sum > k:
        return False
    
    if index >= len(num):
        return False
    
    subset.append(num[index])
    sum += num[index]

    if check(index+1, sum , subset):
        return True
    e = subset.pop()
    sum -= e
    if check(index+1, sum , subset):
        return True

    return False

print(check(0,0,[]))
    
    
 
 