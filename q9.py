n = 5

for i in range(n):

    # left pattern with 0/1 swapped
    for j in range(i + 1):
        print(1 - ((i + j) % 2), end=" ")

    # right side (except last row)
    if i < n - 1:
        spaces = 2 * (n - i - 1) - 2
        print(" " * spaces, end="")
        print(n - i)
    else:
        print()
