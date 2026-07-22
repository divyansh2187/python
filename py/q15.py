n = [5,4,6,4,7,9,8,7,2,2,2,5,5,111,5,6,8,4,67,67,66,10]
m = [10,111,1,9,67,2,5]

# approach 1
# for num in m:
#     count=0
#     for x in n:
#         if num == x:
#             count +=1
#     print(num ,"=", count)


# approach 2

# list = [0,0,0,0,0,0,0,0,0,0,0,]

# for num in n:
#     list[num] += 1 
# print(list)

# for num in m:
#     if num<0 or num>10:
#         # print(num,"=" ,0)
#         pass
#     else:
#         print(num ,"=",list[num])


# approach 3

# dic={}
# for x in n:
#     dic[x]= dic.get(x,0)+1
# for x in m:
#     if x in dic:
#          print(x,"=",dic[x])
#     else:
#        print(x,"=",0)



