import sys
input = sys.stdin.readline

n = int(input())

def fib(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(n))
