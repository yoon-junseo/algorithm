import sys
input = sys.stdin.readline

stations = []

for _ in range(10):
    stations.append(list(map(int, input().split())))

answer = []
sum = 0

for s in stations:
    num = s[1] - s[0]
    sum += num
    answer.append(sum)

print(max(answer))