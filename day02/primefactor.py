def check(n):
    if n <= 1:
        return []
    for i in range(2, n + 1):
        if n % i == 0:
            return [i] + check(n // i)


print(check(24))
