from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
virusList = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 위치(i, j)
            virusList.append((graph[i][j], 0, i, j))


# 시간, 위치(x, y)
s, x, y = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virusList.sort()
q = deque(virusList)

def bfs():
    while q:
        virus, time, x, y = q.popleft()
        
        if time == s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))
        

bfs()
if graph[x - 1][y - 1] == 0:
    print(0)
else:
    print(graph[x - 1][y - 1])
