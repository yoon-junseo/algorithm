import sys

n, m = map(int, sys.stdin.readline().split())

minimum = 0
answer = 0

for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    minimum = min(data)

    if answer < minimum:
        answer = minimum

print(answer)