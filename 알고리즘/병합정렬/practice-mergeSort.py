def mergeSplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergeSplit(data[:medium])
    right = mergeSplit(data[medium:])

    return merge(left, right)


def merge(left, right):
    mergedList = list()
    leftIdx = 0
    rightIdx = 0
    # left, right 모두 남아있는 경우
    while leftIdx < len(left) and rightIdx < len(right):
        if left[leftIdx] > right[rightIdx]:
            mergedList.append(right[rightIdx])
            rightIdx += 1
        else:
            mergedList.append(left[leftIdx])
            leftIdx += 1

    # left만 남아있는 경우
    while leftIdx < len(left):
        mergedList.append(left[leftIdx])
        leftIdx += 1

    # right만 남아있는 경우
    while rightIdx < len(right):
        mergedList.append(right[rightIdx])
        rightIdx += 1

    return mergedList


data = [1, 5, 2, 3, 9, 6, 7]
merged = mergeSplit(data)
print(merged)
