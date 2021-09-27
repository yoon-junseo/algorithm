# 미래도시
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 0으로
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 목표지점, 거쳐갈 곳
x, k = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)