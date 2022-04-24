import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
operand = list(map(int, input().split()))

minResult = 1e9
maxResult = -1e9

def dfs(cnt, num, plus, minus, multi, divide):
    global minResult, maxResult

    if cnt == n:
        minResult = min(num, minResult)
        maxResult = max(num, maxResult)
        return 
    
    if plus:
        dfs(cnt + 1, num + data[cnt], plus - 1, minus, multi, divide)
    if minus:
        dfs(cnt + 1, num - data[cnt], plus, minus - 1, multi, divide)
    if multi:
        dfs(cnt + 1, num * data[cnt], plus, minus, multi - 1, divide)
    if divide:
        dfs(cnt + 1, int(num / data[cnt]), plus, minus, multi, divide - 1)

dfs(1, data[0], operand[0], operand[1], operand[2], operand[3])
print(maxResult)
print(minResult)