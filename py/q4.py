n = 10

odd =[i for i in range(1,n+1)if i %2 == 1][::-1]
even =[i for i in range(1,n+1)if i %2 == 0]

result = odd + even
print(result)