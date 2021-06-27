# Tree

## 설명

- 트리 : Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
- 이진 트리 형태의 구조를 보통 사용하며, 탐색 알고리즘 구현에 많이 사용된다.
- root 노드를 기반으로 좌, 우로 뻗어 나간다.

## 용어

- Node : 트리에서 데이터를 저장하는 기본 요소 (value, left, right의 정보를 갖는다)
- Root Node : 트리의 맨 위에 있는 노드
- Level : 최상위 노드를 Level 0으로 하였을 때, 하위 branch로 연결된 노드의 길이를 나타냄
- Parent Node : 현재 노드에 대해서 상위에 위치한 노드
- Child Node : 현재 노드에 대해서 하위에 위치한 노드
- Leaf Node : Child Node가 하나도 없는, 맨 마지막에 위치한 노드
- Sibling Node : 동일한 Parent Node를 가진 노드, 같은 Level을 갖는다.
- Depth : 트리에서 Node가 가질 수 있는 최대 Level

## 이진트리 (BST)

- 자식 노드가 최대 2개인 노드들로 구성된 트리를 의미한다.
- 왼쪽 노드는 항상 Parent Node 보다 작은 값이 오고, 오른쪽 노드에는 큰 값이 온다.
