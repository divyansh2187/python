# 
# 
# DSA in Python - Minimum Bit Flips to Convert Number | Bit Manipulation | Leetcode 2220 - Part 66
# 
# ---------- checking every bit--------
# def minimunFlips(start , goal):
#     dif = start ^ goal
#     count = 0
#     for i in range(0,32):
#         if dif &(1<<i) !=0:
#             count+=1
#     return count




# ------bit extraction method----------------
# def minimunFlips(start , goal):
#     dif = start ^ goal
#     count = 0
#     while dif>0:
#         if dif%2!=0:
#             count+=1
#         dif = dif//2

#     return count


# print(minimunFlips(10,7))



