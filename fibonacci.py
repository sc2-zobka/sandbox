# 1. Fibonacci Sequence using Raw-Recursion ( not memory efficient )

n = int(input(f'ingrese numero: ' ))

def fib(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    elif n>2:
        return fib(n-1) + fib(n-2)

print(fib(n))
# 0, 1, 1, 2, 3, 5

for k in range(0,n+1):
    print(f'Termino {k+1} : {fib(k)}')

# 2. Fibonacci Sequence using Memoization aka Cache Values

# 2.1 Explicit Memoization Implementation

# create a dict to store how many times fibonacci function's called itself
fib_cache = {}

def fib(n):
    # if value is cached, then return it
    if n in fib_cache:
        return fib_cache[n]
    
    # compute de nth term of fib(n)
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    elif n>2:
        value =  fib(n-1) + fib(n-2)
        
    # cache value and return it
    fib_cache[n] = value
    return value

for k in range(0, n+1):
    print(fib(k))

# 2.2 Memoization Implementation using LRU(Least, Recently, Used) Cache
from functools import lru_cache

@lru_cache(1000)
def fib(n):
    # check Type of argument is a Positive Integer
    if type(n) != int:
        raise TypeError("Argument must be a positve integer")
    if n < 0:
        raise ValueError("Argument must be a positve integer")
    
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    elif n>2:
        return fib(n-1) + fib(n-2)

for k in range(0, n+1):
    print(fib(k))