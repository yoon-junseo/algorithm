# 파이썬 문법 정리

## 스택

```javascript
stack = []
stack.append(5)
stack.append(4)
stack.append(2)
stack.append(7)
stack.append(8)
stack.append(1)
stack.append(9)
stack.append(10)

stack.pop() # 10
stack.pop() # 9

stack.pop(0) # 5 / 비효율적인 방법
```

- append() : 리스트의 가장 뒤쪽에 데이터를 삽입
- pop() : 리스트의 가장 뒤쪽에서 데이터를 꺼낸다.

## 큐

```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.append(4)
queue.append(1)
queue.append(2)

queue.popleft() # 5
queue.popleft() # 2
```

## 리스트 한 줄에 출력

1. sep 이용

```python
a = [0, 1, 2, 3]
print(*a, sep='\n')
```

2. join 이용

```python
a = [0, 1, 2, 3]
print('\n'.join(map(str, answer)))
# 리스트의 요소가 int형인 경우 str로 변환해서 join 해야 한다.
```
