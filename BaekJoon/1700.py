import sys
input = sys.stdin.readline

<<<<<<< Updated upstream
n, k = map(int, input().split())
itemList = list(map(int, input().split()))
multi = [0] * n
=======
>>>>>>> Stashed changes
answer = int(0)
index = int(0)
maxIndex = int(0)
swap = int(0)

<<<<<<< Updated upstream
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
=======
n, k = map(int, input().split())
consent = [0 for _ in range(n)]
itemList = list(map(int, input().split()))
# itemList.sort()

for item in itemList:
    # 콘센트에 이미 꽂혀있는 경우
    if item in consent:
        continue
    # 콘센트에 빈자리가 남은 경우
    elif 0 in consent:
        consent[consent.index(0)] = item
    # 새로 콘센트에 꽂아야 하는 경우
    else:
        for c in consent:
            print(c, item)
            if c not in itemList[index:]:
                swap = c
                
                break
            else:
                index += 1
            # if max
            # print(itemList, itemList[index:], swap, index)
        print    
# print(answer)
>>>>>>> Stashed changes
