from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    if len(g) > 0:
        g.sort()

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

def dfs(graph, v, visited1):
    visited1[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited1[i]:
            dfs(graph, i, visited1)

def bfs(graph, v, visited2):
    q = deque([v])
    visited2[v] = True

    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in graph[now]:
            if not visited2[i]:
                visited2[i] = True
                q.append(i)

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)