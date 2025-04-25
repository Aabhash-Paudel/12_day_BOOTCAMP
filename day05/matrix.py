import random


def isValidGrid(matrix: list[list[int]]) -> bool:
    totalSum = 0
    outer = 0
    outer = outer + sum(matrix[0])
    outer = outer + sum(matrix[-1])

    for i in range(1, len(matrix[0]) - 1):
        row = matrix[i]
        outer += row[0]
        outer += row[-1]

    for i in matrix:
        totalSum += sum(i)

    inner = totalSum - outer
    return inner == outer


def makeMatrix(row: int, col: int):
    return [[random.randint(1, 100) for _ in range(row)] for _ in range(col)]


def solution(row: int, col: int):
    matrix = makeMatrix(row, col)
    while not isValidGrid(matrix):
        matrix = makeMatrix(row, col)
        if isValidGrid(matrix):
            return matrix


result = solution(20, 20)

for row in result:
    print(row)
