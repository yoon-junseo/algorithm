from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True # 방문 처리
    
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and int(graph[nx][ny]) == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = int(graph[a][b]) + 1

bfs(0, 0)
print(graph[n - 1][m - 1])