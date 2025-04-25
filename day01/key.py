def sumDigit(n):
    x = sum([int(i) for i in str(n)])
    return x


def big(n):
    x = [int(i) for i in str(n)]
    max = 0
    for i in x:
        max = i
        if i > max:
            max = i
    return max


def small(n):
    x = [int(i) for i in str(n)]
    min = 0
    for i in x:
        min = i
        if i < min:
            min = i
    return min


def key(i1, i2, i3):
    maxi = big(i1) + big(i2) + big(i3)
    mini = small(i1) + small(i2) + small(i3)
    key = sumDigit(maxi) + sumDigit(mini)
    return key


print(key(1234, 3454, 7976))
