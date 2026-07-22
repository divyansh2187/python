arr = [5,9,1,2,4,15,6,3]


def func(nums,k):
     dic = {}
     for i in range(0,len(nums)):
          remaning = k-arr[i]
          if remaning in dic:
               return [dic[remaning],i]
          dic[nums[i]] = i
         





# def func(arr , t):

#     for i in range (len(arr)-1):
#         for j in range (i+1 , len(arr)):
#            if arr[i]+arr[j] == t:
#                return i,j


print(func(arr,13))