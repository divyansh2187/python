arr = [1,2,8,4,5]

def func(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        isSwpped = False
        for j in range(0,i+1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                isSwpped = True
        if not isSwpped:
            print("Already Sorted")  
            break   
              
func(arr)
print(arr)
            
