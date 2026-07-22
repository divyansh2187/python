tup = (1,3,4,2,5,6,85,77,55,3,66,99,6)
x= int(input("index x : "))
i = 0
while i < len(tup):
   if(x == tup[i]):
     print("at index", i, " value",tup[i]);
   i +=1
    