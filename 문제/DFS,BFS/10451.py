# dfs

import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n = int(input())

def dfs(start):
    visited[start] = True
    number = numbers[start]
    
    if visited[number] == False:
        dfs(number)

for _ in range(n):
    m = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * m
    result = 0

    for i in range(1, m + 1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)
