from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

q = deque([])
q.append((a, 1))

while q:
    num, time = q.popleft()

    if num == b:
        print(time)
        exit(0)

    if num * 2 <= b:
        q.append((num * 2, time + 1))
    
    num = str(num) + '1'
    num = int(num)

    if num <= b:
        q.append((num, time + 1))

print(-1)
