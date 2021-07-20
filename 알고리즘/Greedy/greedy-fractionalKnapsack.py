dataList = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def getMaxValue(dataList, capacity):
    dataList = sorted(dataList, key=lambda x: x[1]/x[0], reverse=True)
    totalValue = 0
    details = list()
    
    for data in dataList:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            totalValue += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            totalValue += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return totalValue, details

print(getMaxValue(dataList, 60))