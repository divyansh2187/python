arr = [1,0,1,1,0,0,1,1,1,1,1,0]

def func(arr):
    count = 0
    maxCount = 0
    for i in arr:
        if i == 1:
            count +=i
        else:
            maxCount = max(maxCount, count)
            count = 0
    return max(maxCount, count )
        
            
print(func(arr))


