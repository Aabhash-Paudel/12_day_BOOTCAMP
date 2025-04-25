"""
12 = 1^2 + 2^2 = 1 + 2 = 3
"""


def sqrSum(num):
    numStr = str(num)
    ans = 0
    for i in numStr:
        ans += int(i) ** 2
    return ans


def round(num):
    while num >= 1:
        cycle = set()
        if num in cycle:
            return False
        if num == 1:
            return True
        num = sqrSum(num)
        cycle.add(num)


print(round(int(input())))
