arr = [1,2,3,4,5,6,7,8,9,10]
k = 4

k = k % len(arr)
rotated = arr[-k:] + arr[:-k]

print(rotated)