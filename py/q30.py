arr = [1,2,3,4,5,6,7,8,9,10]

def funcc(arr):
    temp = arr[-1]
    for i in range(len(arr)-2 ,-1,-1):
        arr[i+1]=arr[i]
        if i == 0:
            arr[0]= temp

funcc(arr)
print(arr) 

