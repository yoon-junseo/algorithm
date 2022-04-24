import heapq
import sys
input = sys.stdin.readline

n = int(input())
numList = []
answer = int(0)

for _ in range(n):
    heapq.heappush(numList, int(input()))

while len(numList) != 1:
    first = heapq.heappop(numList)
    second = heapq.heappop(numList)
    sum = first + second
    answer += sum
    heapq.heappush(numList, sum)
print(answer)