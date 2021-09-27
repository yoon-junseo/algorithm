import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(data)
answer = 0

while start <= end:
    remain = 0
    mid = (start + end) // 2
    for ddeok in data:
        if ddeok > mid:
            remain += ddeok - mid
    if remain > m:
        start = mid + 1
        answer = m
    else:
        end = mid - 1
print(answer)