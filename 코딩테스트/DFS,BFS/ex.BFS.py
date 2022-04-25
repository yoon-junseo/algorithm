# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     # 처음으로 시작하는 노드 방문 처리
#     visited[start] = True
    
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
        
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9
# bfs(graph, 1, visited)
N, K = map(int, input().split())

#각 위치에 도달하는데 이동한 횟수를 담는다.
discovered = [-1 for _ in range(100001)] 

#각 위치에 도달하는 방법수
paths=[0 for _ in range(100001)] 

def bfs():
    queue=[N] # 시작 위치를 넣어준다.
    discovered[N] =0 #첫 번째 위치는 이동 횟수 0번
    paths[N] = 1  #방법수를 1 채워준다.

    while queue:
        loc = queue.pop(0)
        print(loc) 
		
        # 새롭게 움직이는 위치에 대해
        for nloc in [loc +1, loc-1, 2*loc]:
        	#새 위치가 범위안에 있고
            if 0 <= nloc < 100001:
            	#아직 발견이 되지 않았다면 
                if discovered[nloc] == -1:
                	#새로운 위치까지 걸리는 이동횟수 = 이전 위치까지 도달하는데 걸린 이동횟수 +1 
                    discovered[nloc] =discovered[loc] +1
                    #방법수는 동일하다
                    paths[nloc] = paths[loc]
                    queue.append(nloc)
                #만약 새위치가 이전에 방문했던 곳이라면 방법수가 늘어난다.
                else: 
                	#이동 횟수가 최소값인지 확인하고
                    if discovered[nloc] == discovered[loc] +1:
                    	#이전 위치 까지 도달하는 방법수를 더해준다
                        paths[nloc] += paths[loc]

    return

bfs()
print(discovered[K])
print(paths[K])