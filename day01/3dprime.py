"""
3d prime number

number should be
- prime
- sum of digits should be prime
- number of digits should be prime
"""

number = int(input("Enter the no of prime"))


def isPrime(n):
    """Check if int is prime or not"""
    if n <= 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def sumDigit(n):
    x = sum([int(i) for i in str(n)])
    if isPrime(x):
        return True
    return False


def digit(n):
    digi = 0
    while n > 0:
        n = n // 10
        digi += 1
    if isPrime(digi):
        return True
    return False


count = 0
num = 10
prime = []
while True:
    if count == number:
        break
    if isPrime(num):
        if sumDigit(num) and digit(num):
            count += 1
            prime.append(num)
    num += 1
print(prime)
