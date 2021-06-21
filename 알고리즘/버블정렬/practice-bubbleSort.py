def bubbleSort(items):
    length = len(items)

    for i in range(length - 1):
        swap = False
        for j in range(length - i - 1):
            if items[j] > items[j + 1]:
                tmp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = tmp
                swap = True
        if swap == False:
            break


n = int(input('몇 개?'))
items = list(map(int, input('정렬할 아이템(한 줄로 입력)').split()))

bubbleSort(items)
print(items)
