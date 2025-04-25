x = 123


def isCoPrime(i, j, k):
    for n in range(i, x):
        if i % n == 0 and j % n == 0 and k % n == 0:
            return False
        else:
            return True


for i in range(5, x):
    for j in range(4, i):
        for k in range(3, j):
            if j * j + k * k == i * i:
                if isCoPrime(i, j, k):
                    print(f"{k} {j} {i}")
