import sys

number = sys.stdin.readline()
dataList = list()

for i in range(len(number) - 1):
    dataList.append(number[i])

dataList.sort(reverse=True)
print(''.join(dataList))
