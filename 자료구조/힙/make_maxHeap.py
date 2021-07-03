class Heap:
    def __init__(self, data):
        self.heapArray = list()
        self.heapArray.append(None)
        self.heapArray.append(data)

    def moveUp(self, insertedIdx):
        if insertedIdx <= 1:
            return False

        parentIdx = insertedIdx // 2
        if self.heapArray[insertedIdx] > self.heapArray[parentIdx]:
            return True
        else:
            return False

    def insert(self, data):
        # 루트 노드가 없는 경우
        if len(self.heapArray) == 0:
            self.heapArray.append(None)
            self.heapArray.append(data)
            return True

        self.heapArray.append(data)

        insertedIdx = len(self.heapArray) - 1

        # 값을 바꿈
        while self.moveUp(insertedIdx):
            parentIdx = insertedIdx // 2
            tmp = self.heapArray[parentIdx]
            self.heapArray[parentIdx] = self.heapArray[insertedIdx]
            self.heapArray[insertedIdx] = tmp
            insertedIdx = parentIdx

        return True

    def moveDown(self, poppedIdx):
        leftChildIdx = poppedIdx * 2
        rightChildIdx = poppedIdx * 2 + 1

        # 자식 노드가 아예 없는 경우
        if leftChildIdx >= len(self.heapArray):
            return False
        # 오른쪽 자식 노드만 없는 경우
        elif rightChildIdx >= len(self.heapArray):
            if self.heapArray[poppedIdx] < self.heapArray[leftChildIdx]:
                return True
            else:
                return False
        # 자식 노드가 모두 있는 경우
        else:
            if self.heapArray[leftChildIdx] > self.heapArray[rightChildIdx]:
                if self.heapArray[poppedIdx] < self.heapArray[leftChildIdx]:
                    return True
                else:
                    return False
            else:
                if self.heapArray[poppedIdx] < self.heapArray[rightChildIdx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heapArray) <= 1:
            return None

        returnedData = self.heapArray[1]
        self.heapArray[1] = self.heapArray[-1]  # 맨 마지막 데이터를 루트로 가져옴
        del self.heapArray[-1]
        poppedIdx = 1

        while self.moveDown(poppedIdx):
            leftChildIdx = poppedIdx * 2
            rightChildIdx = poppedIdx * 2 + 1

            # 오른쪽 자식 노드가 없는 경우
            if rightChildIdx >= len(self.heapArray):
                self.heapArray[poppedIdx], self.heapArray[leftChildIdx] = self.heapArray[leftChildIdx], self.heapArray[poppedIdx]
                poppedIdx = leftChildIdx

            # 자식 노드가 있는 경우
            else:
                if self.heapArray[leftChildIdx] > self.heapArray[rightChildIdx]:
                    if self.heapArray[poppedIdx] < self.heapArray[leftChildIdx]:
                        self.heapArray[poppedIdx], self.heapArray[leftChildIdx] = self.heapArray[leftChildIdx], self.heapArray[poppedIdx]
                        poppedIdx = leftChildIdx
                else:
                    if self.heapArray[poppedIdx] < self.heapArray[rightChildIdx]:
                        self.heapArray[poppedIdx], self.heapArray[rightChildIdx] = self.heapArray[rightChildIdx], self.heapArray[poppedIdx]
                        poppedIdx = rightChildIdx

        return returnedData


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
data = heap.pop()

print(heap.heapArray)
print(data)
