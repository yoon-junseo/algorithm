import sys
n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort(reverse=True)

for i in range(len(array)):
    print(array[i], end=" ")