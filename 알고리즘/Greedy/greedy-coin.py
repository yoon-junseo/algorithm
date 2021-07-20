coinList = [500, 100, 50, 1]

def minCoinCount(price, coinList):
    totalCoinCount = 0
    details = list()
    coinList.sort(reverse=True)

    for coin in coinList:
        coinNum = price // coin
        totalCoinCount += coinNum
        price -= coinNum * coin
        details.append([coin, coinNum])

    return totalCoinCount, details 

print(minCoinCount(4720, coinList))
