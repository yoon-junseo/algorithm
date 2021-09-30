# import sys
# input = sys.stdin.readline

# n = int(input())
# k = int(input())
# data = [[0] * (n + 1) for _ in range(n + 1)]
# info = [] # 회전 정보

# # 사과는 1로
# for _ in range(k):
#     a, b = map(int, input().split())
#     data[a][b] = 1

# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     info.append((int(x), c))

# # 동, 남, 서, 북
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def turn(direction, c):
#     if c == 'D':
#         direction = (direction + 1) % 4
#     elif c == 'L':
#         direction = (direction - 1) % 4
#     return direction

# def solve():
#     x, y = 1, 1 # 뱀의 머리 위치
#     data[x][y] = 2
#     direction = 0
#     time = 0
#     index = 0
#     q = [(x, y)]

#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]

#         if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#                 px, py = q.pop(0)
#                 data[px][py] = 0
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#         else:
#             time += 1
#             break
#         time += 1
#         x, y = nx, ny
#         if index < l and time == info[index][0]:
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time

# print(solve())


import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 회전 정보

# 사과 정보
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction

def solution():
    x, y = 1, 1
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            else:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        
        time += 1
        x, y = nx, ny

        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(solution())

























