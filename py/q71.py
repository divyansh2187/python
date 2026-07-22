
# DSA in Python - Single Number | Bit Manipulation & XOR Trick | Leetcode 136 - Part 67 [Hindi]

# -------brute force approach--------
# def singleNumber(arr):
#     dic = {}
#     for i in arr:
#             dic[i] = dic.get(i, 0) + 1
#     for key in dic:
#         if dic[key] == 1:
#             return key
# print(singleNumber([4,1,2,1,2]))


# ------------optimized approach-------------

# def singleNumber(arr):
#     ans = 0
#     for i in arr:
#           ans = ans ^ i
#     return ans
# print(singleNumber([7,1,2,1,2]))