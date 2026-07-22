
def funcc(num):
    if num == 0 or num == 1:
        return num
    return funcc(num-1)+funcc(num-2)

print(funcc(5))
    

    
