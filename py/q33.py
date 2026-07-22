num1 = [1,2,3,4,5]
num2 = [4,6,9,10]

def merge(num1 , num2):
    result = []
    n,m= len(num1) , len(num2)
    i,j=0,0
    while i<n and j<m:
        if num1[i] <= num2[j]: 
            if not result or result[-1] != num1[i]:
                result.append(num1[i])
            i +=1
        else:
            if not result or result[-1] != num2[j]:
                result.append(num2[j])
            j +=1
    if  i < n:
        while i < n:
            if not result or result[-1] != num1[i]:
                result.append(num1[i])
            i +=1
    if j < m:
        while j < m:
            if not result or result[-1] != num2[j]:
                result.append(num2[j])
            j +=1
    return result


print(merge(num1,num2))
