nums = [3,6,8,10,1,2,1]

def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while i <= high and nums[i] <= pivot:
            i+=1
        while j >= low  and nums[j] > pivot:
            j-=1
        if i < j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j] = nums[j],nums[low]
    return  j

def quick_sort(nums, low,high): 

    if low < high:
        p_idx = partition(nums , low , high)
        quick_sort(nums , low , p_idx-1 )
        quick_sort(nums , p_idx+1 , high )

quick_sort(nums,0,len(nums)-1)
print(nums)



