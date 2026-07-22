nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]





# -----------------optimal solution-----------------
def func1(num):
   if len(num) == 0:
       return 0
   i = 0
   j = i+1
   while j < len(num):
       if num[i] != num[j]:
           i += 1
           num[i],num[j] = num[j],num[i]
       j+=1
   print(num)
   return i+1
print(func1(nums))
       











# ------------brute force ---------- --------
def funcc(nums):
    freq_map = {}
    

    for i in range(0, len(nums)):
        freq_map[nums[i]] = 0
    freq_map = dict(sorted(freq_map.items()))

    for k in freq_map:
        nums[k-1] = k
    print(nums)

    return len(freq_map)

# print(funcc(nums))