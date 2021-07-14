import sys

n = int(sys.stdin.readline())
dataList = [0 for i in range(10001)]

for i in range(n):
    number = int(sys.stdin.readline())
    dataList[number] += 1

for i in range(len(dataList)):
    if dataList[i] != 0:
        for j in range(dataList[i]):
            print(i)
