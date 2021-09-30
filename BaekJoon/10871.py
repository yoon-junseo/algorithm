import sys
input = sys.stdin.readline

n, x = map(int, input().split())

data = list(map(int, input().split()))

for num in data:
    if num < x:
        print(num, end=' ')