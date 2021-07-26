import sys;
n = int(sys.stdin.readline())
x = int(1)
y = int(1)

moveList = sys.stdin.readline().split()

for m in moveList:
    if m == 'R':
        if y == n:
            continue
        y += 1
    elif m == 'L':
        if y == 1:
            continue
        y -= 1
    elif m == 'D':
        if x == n:
            continue
        x += 1
    elif m == 'U':
        if x == 1:
            continue
        x -= 1

print(x, y)