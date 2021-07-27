import sys
# 배열 사이즈
n, m = map(int, sys.stdin.readline().split())
# 방문한 곳
visited = [[0] * m for _ in range(n)]
x, y, dir = map(int, sys.stdin.readline().split())
visited[x][y] = 1

# 맵 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
array[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = [0, 1, 2, 3] # 북 동 남 서

answer = 1

while (1):
    # 왼쪽으로 회전
    dir -= 1
    if dir == -1:
        dir = 3
    nx = x + int(dx[dir])
    ny = y + int(dy[dir])

    # 회전 이후, 앞에 가보지 않은 칸이 존재하는 경우
    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        visited[nx][ny] = 1
        array[nx][ny] = 1
        x = nx
        y = ny
        answer += 1
        continue
    # 회전 이후, 앞에 바다거나 가본칸인 경우
    elif visited[nx][ny] == 1 and array[nx][ny] == 1:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if array[nx][ny] == 0:
            x = nx
            y = ny

    # n줄에 모두 1인 경우 탈출
    exit_cnt = 0
    for a in array:
        if 0 not in a:
            exit_cnt += 1
    if exit_cnt == n:
        break
print(answer)