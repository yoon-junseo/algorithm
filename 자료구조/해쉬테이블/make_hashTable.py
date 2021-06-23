hashTable = list([0 for i in range(10)])


def hashFunc(key):
    return key % 5


def storageData(data, value):
    key = ord(data[0])
    hashAddress = hashFunc(key)
    hashTable[hashAddress] = value


def getData(data):
    key = ord(data[0])
    hashAddress = hashFunc(key)
    return hashTable[hashAddress]


storageData('junseo', '1234')
storageData('zzz', '3333')

print(hashTable)

print(getData('junseo'))
