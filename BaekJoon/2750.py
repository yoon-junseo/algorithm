import sys

n = int(input())
dataList = list()

for i in range(n):
    data = int(sys.stdin.readline())
    if data not in dataList:
        dataList.append(data)

dataList.sort()
for i in range(len(dataList)):
    print(dataList[i])
