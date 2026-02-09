n = 5

for i in range(1,n+1):
    val = i%2
    for k in range(i):
        print(val,end="")
        val = 1-val
    print()