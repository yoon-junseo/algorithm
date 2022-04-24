# 실전 문제 - 음료수 얼려 먹기
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# def dfs(x, y):
#     graph[x][y] = 1
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         dfs(x, y - 1)
#         return True
#     return False

# answer = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             answer += 1
#             print(i, j)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    if graph[x][y] == 1:
        return False

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny))
    return True

answer = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            answer += 1
        
print(answer)
