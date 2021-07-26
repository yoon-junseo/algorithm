import sys

pos = sys.stdin.readline()
x = int(pos[1])
y = int(ord(pos[0]) - 96)
moveList = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
answer = 0

for m in moveList:
    if (x + m[0] > 8) or (x + m[0]) < 1:
        continue
    elif (y + m[1] > 8) or (y + m[1]) < 1:
        continue
    answer += 1

print(answer)