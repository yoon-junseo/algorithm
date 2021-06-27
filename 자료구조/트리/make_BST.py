class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeManagement:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            # 왼쪽으로 순회
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            # 오른쪽으로 순회
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False

        # 노드 삭제
        else:
            # 루트 노드 삭제
            if self.current_node.left == None and self.current_node.right == None:
                if value < self.current_node.value:
                    self.parent.left = None
                else:
                    self.parent.right = None
                del self.current_node

            # 왼쪽 자식 노드만 존재
            elif self.current_node.left != None and self.current_node.right == None:
                if value < self.parent.value:
                    self.parent.left = self.current_node.left
                else:
                    self.parent.right = self.current_node.left
            # 오른쪽 자식 노드만 존재
            elif self.current_node.left == None and self.current_node.right != None:
                if value < self.parent.value:
                    self.parent.left = self.current_node.right
                else:
                    self.parent.right = self.current_node.right
            # 자식 노드가 모두 존재
            elif self.current_node.left != None and self.current_node.right != None:

                # 삭제할 값이 왼쪽 노드에 존재
                if value < self.parent.value:
                    self.change_node = self.current_node.right
                    self.change_node.parent = self.current_node.right
                    while self.change_node.left != None:
                        self.change_node.parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change_node.right != None:
                        self.change_node.parent.left = self.change_node.right
                    else:
                        self.change_node.parent.left = None
                    self.parent.left = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.current_node.left
                # 삭제할 값이 오른쪽 노드에 존재
                else:
                    self.change_node = self.change_node.right
                    self.change_node.parent = self.current_node.right
                    while self.change_node.right != None:
                        self.change_node.parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change_node.right != None:
                        self.change_node.parent.left = self.change_node.right
                    else:
                        self.change_node.parent.left = None
                    self.parent.right = self.change_node
                    self.change_node.left = self.current_node.left
                    self.change_node.right = self.current_node.right


head = Node(1)
BST = NodeManagement(head)
BST.insert(2)
print(BST.search(2))

BST.delete(2)
print(BST.search(2))
