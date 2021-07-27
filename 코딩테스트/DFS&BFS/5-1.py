import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    # 아직 방문하지 않은 그래프
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y) # 상
        dfs(x + 1, y) # 하
        dfs(x, y - 1) # 좌
        dfs(x, y + 1) # 우
        return True
    return False

answer = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)
        
