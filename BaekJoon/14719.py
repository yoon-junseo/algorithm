import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rain = list(map(int, input().split()))

data = [[0] * m for _ in range(n)]
answer = int(0)

for i in range(len(rain)):
    cnt = rain[i]
    for j in range(n - 1, -1, -1):
        if cnt:
            data[j][i] = 1
            cnt -= 1

for i in range(n):
    temp = int(0)
    rain1 = False # 처음 1
    rain2 = False # 마지막 1
    for j in range(m):
        if data[i][j] == 1:
            rain1 = True
            if temp > 0:
                answer += temp
                temp = 0
        elif data[i][j] == 0 and rain1:
            temp += 1
        elif data[i][j] == 1 and j == m - 1:
            answer += temp
            
print(answer)
