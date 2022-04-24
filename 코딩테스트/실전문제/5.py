import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ball = list(map(int, input().split()))
ball.sort()

answer = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if ball[i] != ball[j]:
            answer += 1

print(answer)
