# 플로이드 워셜

import sys 
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 및 간선
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 것은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 수행
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('INF', end=" ")
        else:
            print(graph[i][j], end=" ")
    print()