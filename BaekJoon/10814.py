import sys

n = int(sys.stdin.readline())
dataList = list()

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    dataList.append((int(age), name))

dataList.sort(key=lambda x: (x[0]))

for i in range(len(dataList)):
    print(dataList[i][0], dataList[i][1])
