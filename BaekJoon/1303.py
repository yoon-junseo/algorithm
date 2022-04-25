from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
visited = [[False] * n for _ in range(m)]

for _ in range(m):
    graph.append(list(input().rstrip()))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque([])
def bfs(x, y, color):
    q.append((x, y))
    visited[x][y] = True
    cnt = int(1)

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[nx][ny] == color and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

white = int(0)
blue = int(0)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and visited[i][j] == False:
            white += bfs(i, j, 'W') ** 2
        elif graph[i][j] == 'B' and visited[i][j] == False:
            blue += bfs(i, j, 'B') ** 2

print(white, blue)