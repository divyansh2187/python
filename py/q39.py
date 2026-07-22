arr = [5,10,-3,-1,-10,6]

def funca(arr):
    result = [0]*len(arr)
    i =0 
    j = 1

    for k in arr:
        if k >= 0:
            result[i] = k
            i+=2
        else:
            result[j] = k
            j+=2
    return result

print(funca(arr))

















    

# def func(arr):
#     pos = []
#     neg = []
#     for i in arr:
#         if i <= 0:
#             neg.append(i)
#         else:
#             pos.append(i)
#     for i in range(0,len(neg)):
#         arr[i*2] = pos[i]
#         arr[(i*2)+1]=neg[i]
#     return arr

# print(func(arr))
            
    



          
        
