#recursion for prime factorization 
def abc(n):
    if n == 1:
        return []
    for i in range(2, n + 1):
        if n % i == 0:
            return [i] + abc(n // i)
        
            
        
n=int(input("Enter number"))
print(abc(n))