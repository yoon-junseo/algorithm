import sys
import math
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

answer = int(0)

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def isPrimeAdvanced(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

for num in numbers:
    if isPrimeAdvanced(num):
        answer += 1

print(answer)