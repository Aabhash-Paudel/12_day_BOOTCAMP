import random

def maker(row: int, col: int):
    return [[random.randint(1, 100) for  in range(col)] for  in range(row)]

def summer(matrix: list[list[int]]) -> bool:
    total = 0
    total1 = 0

    total += sum(matrix[0])
    total += sum(matrix[-1])

    for i in range(1, len(matrix) - 1):
        total += matrix[i][0]
        total += matrix[i][-1]

        for j in range(1, len(matrix[i]) - 1):
            total1 += matrix[i][j]

    if total == total1:
        print("Matrix:")
        for row in matrix:
            print(row)
        print("Border sum (total):", total)
        print("Inner sum (total1):", total1)
        print("valid matrix\n")
        return False

    return True

while summer(maker(11,10)):
    pass
