import sys
n, k = map(int, sys.stdin.readline().split())

answer = 0

while n > 1:
    if n % k == 0:
        n = n // k
        answer += 1
    else:
        n -= 1
        answer += 1
        
print(answer)