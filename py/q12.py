
num = 1234  #4321
n=num
result = 0

while n>0:
    ld = n%10
    result = (result * 10)+ld
    n = n//10
if num == result:
    print(num ," = ", result , "palindrome")
else:
    print(num ," != ", result , " not palindrome")

