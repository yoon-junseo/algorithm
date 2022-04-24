from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = int(0)

def bfs(x, y):
    q = deque([])
    q.append((x,y))
    unitedCnt = int(1)
    sum = graph[x][y]

    unitedList = [] # 연합 리스트
    unitedList.append((x, y))
    union[x][y] = True

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == False:
                if L <= abs(graph[a][b] - graph[nx][ny]) <= R:
                    unitedList.append((nx, ny))
                    unitedCnt += 1
                    sum += graph[nx][ny]
                    union[nx][ny] = True
                    q.append((nx, ny))

    newPopulation = sum // unitedCnt
    for x, y in unitedList:
        graph[x][y] = newPopulation

while True:
    union = [[False] * N for _ in range(N)]
    cnt = int(0)
    for i in range(N):
        for j in range(N):
            if union[i][j] == False:
                bfs(i, j)
                cnt += 1
    if cnt == N * N:
        break
    answer += 1

bfs(0, 0)   
print(answer)

