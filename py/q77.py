

# optimal solution is to use recursion to generate all binary strings of length n, ensuring that no two consecutive 1's are present. The function `binary(n)` initializes the process, while the inner function `recursion(idx, flag, num, result)` handles the recursive generation of the binary strings.
def binary(n):

    def recursion(idx , flag , num , result):
        if idx >= len(num):
           return result.append("".join(num))

        num[idx] = "0"
        recursion(idx+1,True,num,result)

        if flag == True:
            num[idx] = "1"
            recursion(idx+1,False,num,result)
            num[idx] = "0"



    result = []
    num = ['0'] * n
    recursion( 0 , True , num , result ) 

    return result


print(binary(3))
    
    

        
# brute force----------------------------

def binary_search(n):
    limit = 1<<n
    fst = []

    for num in range(0,limit):
        correct = True

        for i in range(0,n-1):
            if (num>>i)&1 == 1 and (num>>(i+1))&1 == 1:
                correct = False
                break
            
        if correct == True:
            fst.append(format(num, '0'+str(n)+'b'))

    return fst

# print(binary_search(4))





                
