
arr = [1,2,3,4,5,6,7,8,9,10]

def func(arr , l , r):
    if l >= r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    func(arr , l+1 , r-1)
func(arr , 0 , 5)
print(arr)