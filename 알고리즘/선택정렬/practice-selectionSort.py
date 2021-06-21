n = int(input('몇 개?'))
items = list(map(int, input('정렬할 아이템(한 줄로 입력)').split()))
length = len(items)

for i in range(length - 1):
    min = items[i]
    idx = 0
    swap = False
    for j in range(i+1, length):
        if min > items[j]:
            min = items[j]
            idx = j
            swap = True
    if swap:
        tmp = items[i]
        items[i] = min
        items[idx] = tmp
    print(items)
