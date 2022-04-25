import sys
input = sys.stdin.readline

a, b = map(int, input().split())

answer = int(0)

numbers = []

for i in range(1, 46):
    for _ in range(i):
        numbers.append(i)

for i in range(a - 1, b):
    answer += numbers[i]

print(answer)