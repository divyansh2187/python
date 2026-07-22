# num = int(input("enter a number:"))
# n = num 
# result=[]

# for i in range(1 , (n // 2)+1):
#     if num%i == 0:
#         result.append(i)
# result.append(num)
# print(result)



num = int(input("enter a number:"))
n = num 
result=[]

for i in range(1 , int(n ** 0.5) + 1):
    if num%i == 0:
        result.append(i)
    if i != num//i:
        result.append(num//i) 


result.sort()
print(result)
    
    
    