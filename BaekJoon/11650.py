import sys

n = int(sys.stdin.readline())
pointList = list()

for i in range(n):
    x, y = map(str, sys.stdin.readline().split())
    pointList.append((int(x), int(y)))

pointList.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(pointList[i][0], pointList[i][1])