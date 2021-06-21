class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class NodeManagement:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)  # 새로운 노드 생성
            node.next = new  # 마지막 노드에 새로운 노드 연결
            new.prev = node  # 새로운 노드에 이전 노드 연결
            self.tail = new  # 마지막 노드 세팅

    def printNode(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def searchFromHead(self, data):
        if self.head == None:
            return False

        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def searchFromTail(self, data):
        if self.head == None:
            return False

        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insertBefore(self, data, beforeData):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != beforeData:  # 해당 데이터를 찾을때까지 반복
                node = node.prev
                if node == None:
                    return False
            new = Node(data)  # 삽입할 노드
            beforeNew = node.prev  # 삽입할 위치 이전 노드
            beforeNew.next = new  # 삽입할 위치 이전 노드의 다음으로 새로운 노드 연결
            new.prev = beforeNew  # 새로 삽입할 노드의 이전 노드에 삽입할 위치 이전 노드 연결
            new.next = node  # 새로 삽입할 노드의 다음 노드에 삽입할 위치의 다음 노드 연결
            node.prev = new  # 새로 삽입할 위치의 다음 노드의 이전 노드에 새로운 노드 연결
            return True

    def insertAfter(self, data, afterData):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != afterData:
                node = node.next
            new = Node(data)
            afterNew = node.next
            afterNew.prev = new
            node.next = new
            new.prev = node
            new.next = afterNew
            return True


doubleLinkedList = NodeManagement(0)

for data in range(1, 10):
    doubleLinkedList.insert(data)

doubleLinkedList.insertAfter(11, 5)  # (새로운 데이터, 삽입할 위치)
doubleLinkedList.printNode()
