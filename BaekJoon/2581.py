import sys
import math
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

m = int(input())
n = int(input())

primeList = []
sum = int(0)
minimum = int(0)

for i in range(m, n + 1):
    if isPrime(i):
        primeList.append(int(i))
        sum += i
primeList.sort()

if len(primeList) > 0:
    print(sum)
    print(primeList[0])
else:
    print('-1')