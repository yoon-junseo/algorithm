from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

def bfs(x):
    while q:
        now = q.popleft()

        for nextNode in graph[now]:
            if distance[nextNode] == -1:
                distance[nextNode] = distance[now] + 1
                q.append(nextNode)

bfs(x)

for i in range(len(distance)):
    if distance[i] == k:
        answer.append(i)

if len(answer) > 0:    
    print(*answer, sep='\n')
else:
    print('-1')


























# distance = [-1 for _ in range(n + 1)]
# distance[0] = 0
# distance[x] = 0

# q = deque([x])

# while q:
#     now = q.popleft()
#     for nextNode in graph[now]:
#         if distance[nextNode] == -1:
#             distance[nextNode] = distance[now] + 1
#             q.append(nextNode)

# for i in range(len(distance)):
#     if distance[i] == k:
#         answer.append(i)

# if len(answer) > 0:
#     print(*answer, sep='\n')
# else:
#     print(-1)