
def fectorial(n):
    if n == 1 or n == 0:
        return 1 
    return fectorial(n-1)*n

print(fectorial(5))