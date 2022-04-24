import sys
input = sys.stdin.readline

n, k = map(int, input().split())
itemList = list(map(int, input().split()))
multi = [0] * n
answer = int(0)
index = int(0)
maxIndex = int(0)
swap = int(0)

if k <= n:
    print(0)
    exit(0)
a = 0
for item in itemList:
    a += 1
    if item in multi: # 이미 꽂혀 있는 경우
        pass
    elif 0 in multi: # 빈칸이 있으면 그냥 꽂기
        multi[multi.index(0)] = item
    else:
        for m in multi:
            if m not in itemList[index:]:
                swap = m
                break
            elif itemList[index:].index(m) > maxIndex:
                maxIndex = itemList[index:].index(m)
                swap = m
        multi[multi.index(swap)] = item
        maxIndex = swap = 0
        answer += 1
    index += 1
print(answer)
