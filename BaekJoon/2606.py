from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = int(0)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([])

def bfs(start):
    global answer
    q.append(start)
    visited[start] = True
    
    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                answer += 1

bfs(1)
print(answer)