arr = [1, 20, 3, 18, 5, 6, 7, 8, 18, 1]

def funcc(arr):
    largest = float('-inf')
    second = float('-inf')
    small = float('inf')
    smallest = float('inf')
    for i in range(0,len(arr)):
      if arr[i] > largest:
         second = largest
         largest = arr[i]
      elif arr[i] > second and arr[i]!= largest:
         second = arr[i]

      if arr[i] < smallest:
         small = smallest
         smallest = arr[i]
      elif arr[i] < small and arr[i]!= smallest:
         small = arr[i]
    return second , small
print(funcc(arr))
