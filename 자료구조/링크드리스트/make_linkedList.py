class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMangement:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == None:  # 헤드가 비어있다면 헤드에 데이터 생성
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, data):
        if self.head == None:
            print('해당 값을 가진 노드가 없다.')
            return
        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                else:
                    node = node.next

    def printNode(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


linkedList1 = NodeMangement(0)

for data in range(1, 10):
    linkedList1.add(data)
linkedList1.printNode()

linkedList1.delete(5)
print('-'*10)
linkedList1.printNode()
