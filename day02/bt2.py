def abc(n):
    if n == 1:
        return 2
    b = abc(n - 1)
    print("hai", end=" ")
    return b + 1


print(abc(5))
