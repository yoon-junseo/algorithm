# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []
# temp = [[0] * m for _ in range(n)] # 벽 설치후 맵
# answer = int(0)

# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# # 북 동 남 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 바이러스 퍼뜨리기
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)

# # 점수 계산하기
# def getScore():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score

# # 벽 세우면서 안전 영역 구하기
# def dfs(count):
#     global answer
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = graph[i][j]

#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
        
#         answer = max(answer, getScore())
#         return

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 graph[i][j] = 0
#                 count -= 1

# dfs(0)
# print(answer)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
virusList = []
temp = [[0] * m for _ in range(n)] # 벽 설치후 맵
answer = 0

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def virus():
    q = deque()
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]
            if graph[i][j] == 2:
                q.append([i, j])
    
    while q:
        pos = q.popleft()
        
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny <m: 
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append([nx, ny])

def getScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def wall(cnt):
    global answer
    if cnt == 3:
        virus()
        answer = max(answer, getScore())
        return 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                wall(cnt)
                graph[i][j] = 0
                cnt -= 1

wall(0)
print(answer)
        