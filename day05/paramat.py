import random
from multiprocessing import Pool, cpu_count


def isValidGrid(matrix):
    """Optimized validation with single-loop calculation"""
    n = len(matrix)
    outer = sum(matrix[0]) + sum(matrix[-1])  # First and last rows
    for row in matrix[1:-1]:
        outer += row[0] + row[-1]  # First and last columns
    total = sum(sum(row) for row in matrix)
    return (total - outer) == outer


def makeMatrix(row, col):
    """Matrix generator with pre-allocated memory"""
    return [[random.randint(1, 100) for _ in range(col)] for _ in range(row)]


def worker(args):
    """Parallel worker that generates matrices until valid one found"""
    row, col = args
    while True:
        matrix = makeMatrix(row, col)
        if isValidGrid(matrix):
            return matrix


def solution(row, col):
    """Parallelized solution using multiple workers"""
    num_workers = cpu_count()
    with Pool(num_workers) as pool:
        # Each worker gets a copy of the parameters
        args = [(row, col)] * num_workers
        results = pool.imap_unordered(worker, args)

        # Return first valid result found
        for result in results:
            pool.terminate()  # Stop other workers once we find a solution
            return result


if __name__ == "__main__":
    result = solution(10, 10)
    for row in result:
        print(row)
