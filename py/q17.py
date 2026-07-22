# count = 0

# def func():
#     global count
#     count +=1
#     print(count)
#     if count == 4:
#      return
#     func()

# func()


# def func(x,n):
#     if n==0:
#         return
#     print(x , n)
#     func(x ,n-1)

# func(15,4)


def pri(n):
    if n==0:
      return
    pri(n-1)
    print(n)
pri(10)