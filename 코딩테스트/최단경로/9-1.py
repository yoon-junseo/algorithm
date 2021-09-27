# 다익스트라 (노드와 간선의 개수가 적을때 사용)

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 나타냄

# 노드와 간선의 개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 그래프 정보
graph = [[] for i in range(n + 1)]

# 방문한적이 있나 확인
visited = [False] * (n + 1)

# 최소 거리
distance = [INF] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    # a -> b 로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def getSmallestNode():
    minValue = INF
    idx = 0

    for i in range(1, n + 1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n - 1):
        now = getSmallestNode()
        visited[now] = True
        for j in graph[now]:
            cost = j[1] + distance[now]
            if distance[j[0]] > cost:
                distance[j[0]] = cost                 

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])