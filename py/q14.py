# method2
# num =[1,2,3,2,4,4,2,4,2,4,3,32]
# dic={}

# for i in num:
#     dic[i]=num.count(i)
# print(dic)

# method 2
# num =[1,2,3,2,4,4,2,4,2,4,3,32]
# dic={}

# for i in num:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# print(dic)


num =[1,2,3,2,4,4,2,4,2,4,3,32]
dic={}

for i in num:
    dic[i]=dic.get(i,0)+1
print(dic)