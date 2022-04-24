import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 인접 행렬
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(x, y):
    if x < 0 or x >= n  or y < 0 or y >= m:
         return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))

#     if graph[x][y] == 1:
#         return False
    
#     while q:
#         pos = q.popleft()
#         graph[pos[0]][pos[1]] = 1

#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
        
#             if nx >= 0 and nx < n and ny >= 0 and ny < m:
#                 if graph[nx][ny] == 0:
#                     q.append((nx, ny))
#                     graph[nx][ny] = 2
#     return True

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1
            print(i, j)