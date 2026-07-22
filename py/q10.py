
num = int(input("enter a number:"))
n=num
target = 0
length = len(str(n))

for i in range (length):
    lg = n%10
    target += lg ** length
    n = n//10
if target == num:
    print("armstrong number",target)
else:
    print("not armstrong number",target)
