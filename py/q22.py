arr = [1,4,6,3,6,5,4,8,9,54]


def func(arr):
    n = len(arr)
    for i in range(0,n):
        MinIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[MinIndex]:
                MinIndex = j
        arr[i],arr[MinIndex] = arr[MinIndex],arr[i]

func(arr)
print(arr)  

