import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turnCount = 0

while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if data[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turnCount = 0
        continue
    else:
        turnCount += 1
    
    if turnCount == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turnCount = 0
        
print(count)