
# DSA in Python - Bit Manipulation Basics | Swapping, Setting, Clearing, Toggling Bits - Part 65

# ---------------------------swapping bits-------------------------

# a = 5
# b =10

# a = a^b 
# b = a^b 
# a= a^b
# print(a,b)

# -------------------checking if ith bit is set or not----------------------

# ------------using sift left--------------------
# n =13
# i = 2

# if(n & (1<< i))!=0:
#     print(True)
# else:
#     print(False) 

# ----------using sift rigth------------------------

# n =13
# i = 2
# if ((n>>i)&1)!=0:
#     print(True)
# else:
#     print(False)    
 


# -------------set ith bit----------------------

# n = 13
# i = 1
# new = n | (1<<i)
# print(new)


# -----------set ith bit to off-----------

# n = 13
# i =2
# new = n &(~(1<<i))
# print(new)


# --------------remove the last set bit-----------------

# rigth most------------

# n = 16
# new = n & (n-1)
# print(new)



# ----------------check if a number is power of 2-----------------

# n = 16
# if  (n&(n-1)==0):
#     print(True)
# else:
#     print(False)    


# ---------convert into binary representation-----------------

# def convert2binary(n):
#     result = ""
#     while n>0:
#         if n%2==0:
#             result += "0"
#         else:
#             result += "1"
#         n = n//2
#     return result[::-1]

# print(convert2binary(13))


# -------------binary to decimal-----------------------

# def convert2decimal(N):
#     decimal  = 0
#     power = 0
#     index = len(N)-1
#     while index>=0:
#         num = int(N[index]) 
#         decimal +=num*(2**power)
#         power +=1
#         index -=1
#     return decimal


# print(convert2decimal("1101"))
