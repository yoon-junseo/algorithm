def binarySearch(dataList, findData):
    if len(dataList) == 1 and dataList[0] == findData:
        return dataList[0]
    elif len(dataList) == 1 and dataList[0] != findData:
        return None
    elif len(dataList) == 0:
        return None

    mid = int(len(dataList) / 2)
    if dataList[mid] > findData:
        return binarySearch(dataList[:mid], findData)
    else:
        return binarySearch(dataList[mid:], findData)


dataList = [1, 2, 4, 6, 8]
print(binarySearch(dataList, 8))
