import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))
operandList = list(map(int, input().split()))

minResult = 1e9
maxResult = -1e9

# 숫자 idx, 계산 숫자 num
# 연산자 -> 0: +, 1: -, 2: x, 3: /
def dfs(idx, num):
    global minResult, maxResult
    print(idx, num)
    if idx == n:
        minResult = min(minResult, num)
        maxResult = max(maxResult, num)
    
    else:
        if operandList[0] > 0:
            operandList[0] -= 1
            print('0', operandList)
            dfs(idx + 1, num + numList[idx])
            operandList[0] += 1
            print('zz', idx, num)
        if operandList[1] > 0:
            operandList[1] -= 1
            print('1', operandList)

            dfs(idx + 1, num - numList[idx])
         
            operandList[1] += 1
        if operandList[2] > 0:
            operandList[2] -= 1
            print('2', operandList)

            dfs(idx + 1, num * numList[idx])
            print('bb', idx, num)
            operandList[2] += 1
        if operandList[3] > 0:
            operandList[3] -= 1
            print('3', operandList)

            dfs(idx + 1, int(num / numList[idx]))   
            operandList[3] += 1

dfs(1, numList[0])
print(operandList)
print(maxResult)
print(minResult)
