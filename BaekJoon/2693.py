import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data[2])
