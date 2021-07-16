import sys

number = int(sys.stdin.readline())

def fib(number):
    cache = [0 for i in range(number + 1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, number + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[number]

print(fib(number))