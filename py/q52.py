arr = [1,2,3,3,3,3,4,5,6]

# ----------optimal solution----------
def func(arr,t):
    def lowerB(arr,t):
        low = 0
        high = len(arr)-1
        lowerBound = -1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] >= t:
                high = mid-1
                lowerBound = mid
            else:
                low = mid+1
        return lowerBound
    
    def upperB(arr,t):
        low = 0
        high = len(arr)-1
        upperBound = len(arr)
        while low <= high:
            mid = (low+high)//2
            if arr[mid] > t:
                high = mid-1
                upperBound = mid
            else:
                low = mid+1
        return upperBound
    
    def output(arr ,t):
        lwr = lowerB(arr,t)
        if lwr == len(arr) or arr[lwr] != t:
            return 0 
        upr = upperB(arr,t)
        
        return upr-lwr
    return output(arr,t)

print(func(arr,3))

        







# --------brute force--------
# def func(arr,t):
#     count = 0
#     for i in arr:
#         if i == t:
#             count+=1
#         elif i > t:
#             break
#     return count



