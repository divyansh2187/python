
str = "abba"


def func(str , r , l):
    if l >= r:
        return True
    if str[r] != str[l]:
        return False
    return func(str , r-1, l+1)

print(func(str , len(str)-1 , 0 ))

    






