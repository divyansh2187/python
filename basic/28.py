list = [1, 2, 3, 4, 5]

def sum(list , i=0):
    if (i < len(list)):
        print(list[i])
        return  sum(list , i+1)
    return 0

sum(list)