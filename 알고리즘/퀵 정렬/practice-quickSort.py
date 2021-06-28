def qsort(data):
    if len(data) <= 1:
        return data
    left = list()
    right = list()
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return qsort(left) + [pivot] + qsort(right)


data = [1, 4, 2, 5, 11, 3, 9, 0]
print(qsort(data))
