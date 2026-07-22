num = 5187222 
n=num
count = 0

def countdigi(n):
  while n>0:
   global count
   count += 1
   n=n//10
  print(count)

countdigi(n)