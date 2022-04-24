import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

graph = [] # 그래프 정보
temp = [[0] * n for _ in range(n)] # 장애물 세우고 확인할 임시 공간
teachers = []
spaces = []

for i in range(n):
    graph.append(list(map(str, input().split())))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        if graph[i][j] == 'X':
            spaces.append((i, j))

# 0 ~ 3 -> 좌 우 상 하
def watch(x, y, direction):
    if direction == 0:
        while y >= 0:  
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            y -= 1
        return False

    elif direction == 1:
        while y < n:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O': 
                return False
            y += 1
        return False

    elif direction == 2:
        while x >= 0:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O': 
                return False
            x -= 1
        return False

    elif direction == 3:
        while x < n:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O': 
                return False
            x += 1   
        return False

answer = []
find = True

def check():
    for t in teachers:
        for i in range(4):
            if watch(t[0], t[1], i):
                return True
    return False

def wall(cnt):
    global find
    if cnt > 3:
        return
    if cnt == 3:
        if not check():
            find = False
            return
        else:
            find = True

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                wall(cnt + 1)
                if find == False:
                    return
                graph[i][j] = 'X'
wall(0)

# for data in combinations(spaces, 3):
#     for x, y in data:
#         graph[x][y] = 'O'
#     if not check():
#         find = False
#         break
#     for x, y in data:
#         graph[x][y] = 'X'

if find:
    print('NO')
else:
    print('YES')