# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# x, y, direction = map(int, input().split())

# d = [[0] * m for _ in range(n)]
# d[x][y] = 1

# data = []

# for _ in range(n):
#     data.append(list(map(int, input().split())))

# # 북, 동, 남, 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def turnLeft():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# count = 1
# turnCount = 0

# while True:
#     turnLeft()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     if data[nx][ny] == 0 and d[nx][ny] == 0:
#         d[nx][ny] = 1
#         x, y = nx, ny
#         count += 1
#         turnCount = 0
#         continue
#     else:
#         turnCount += 1
    
#     if turnCount == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         if data[nx][ny] == 0:
#             x, y = nx, ny
#         else:
#             break
#         turnCount = 0
        
# print(count)
n = int(input())

data = []
teacher = []
wall = []
result = "NO"

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i,j))

def check_t():
    global teacher, data
    for t in teacher:
        for i in range(4):
            x, y = t
            while 0<= x < n and 0<= y < n:
                if data[x][y] == 'O':
                    break
                elif data[x][y] == 'S':
                    return False
                x += dx[i]
                y += dy[i]
    return True

def dfs(count):
    global teacher, data, result, wall
    if count > 3:
        return
    if count == 3:
        if check_t() is True:
            result = "YES"
            return
        else:
            result = "NO"
    
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                # wall.append((i,j))
                dfs(count+1)
                if result == "YES":
                    return
                # wall.remove((i,j))
                data[i][j] = 'X'

dfs(0)
print(result)