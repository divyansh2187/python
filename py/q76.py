num = [5,9,4]
k = 9
result = 0
def check(index, sum):
    global result
    if sum == k:
       result+=1
       return 
    
    if sum > k:
        return 
    
    if index >= len(num):
        return 
    
   
    sum += num[index]

    check(index+1, sum )
       
    
    sum -= num[index]
    check(index+1, sum )

       

    return result

print(check(0,0))
    
    
 
 