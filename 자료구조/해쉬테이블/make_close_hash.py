import hashlib

hashTable = list([0 for i in range(8)])


# 랜덤한 hash 데이터
def getKey(data):
    hashObject = hashlib.sha256()  # sha 256 해쉬
    hashObject.update(data.encode())
    hexDigit = hashObject.hexdigest()
    return int(hexDigit, 16)

    # return hash(data)


# hash를 이용한 인덱스 생성
def hashFunc(key):
    return key % 8


def saveData(data, value):
    indexKey = getKey(data)
    hashAddress = hashFunc(indexKey)
    # 같은 키 값을 갖는다면 중복 처리 (key, value 쌍으로 데이터 추가)
    if hashTable[hashAddress] != 0:
        for i in range(hashAddress, len(hashTable)):
            if hashTable[i] == 0:
                hashTable[i] = [indexKey, value]
                return
            # 같은 아이템의 값을 업데이트
            elif hashTable[i][0] == indexKey:
                hashTable[i][1] = value
                return
    else:
        hashTable[hashAddress] = [indexKey, value]


def readData(data):
    indexKey = getKey(data)
    hashAddress = hashFunc(indexKey)

    if hashTable[hashAddress] != 0:
        for i in range(hashAddress, len(hashTable)):
            if hashTable[i] == 0:
                return None
            elif hashTable[i][0] == indexKey:
                return hashTable[i][1]
    else:
        return None


saveData('junseo', '1234')
saveData('jerqeo', '3333')

print('read: ', readData('junseo'))
print(hashTable)
