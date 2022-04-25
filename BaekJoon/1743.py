from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited =[[False] * m for _ in range(n)]
answer = int(0)
t = int(0)

for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global t
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    t += 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                t += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            answer = max(answer, t)
            t = 0

print(answer)
