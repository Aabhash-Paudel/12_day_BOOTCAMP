"""
Spiral Matrix

3x3

1,1 | 1,2 | 1,3 | 2,3 | 3,3 | 3,2 | 3,1 | 2,1 | 2,2

"""

matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 18, 19],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42],
]
spiral = []

top = 0
right = len(matrix[0]) - 1
bottom = len(matrix) - 1
left = 0

while left <= right and top <= bottom:
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top += 1
    print()
    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1
    print()
    for i in range(right, left - 1, -1):
        print(matrix[bottom][i], end=" ")
    bottom -= 1
    print()
    for i in range(bottom, top - 1, -1):
        print(matrix[i][left], end=" ")
    left += 1
    print()
