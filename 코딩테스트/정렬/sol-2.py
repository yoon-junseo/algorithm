import sys
n = int(sys.stdin.readline())

array = []
for i in range(n):
    name, score = sys.stdin.readline().split()
    array.append((name, score))

array.sort(key=lambda x: x[1])

for a in array:
    print(a[0], end=" ")