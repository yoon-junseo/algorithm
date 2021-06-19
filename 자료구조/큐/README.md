# Queue

## 설명

> - FIFO (First In First Out) 형태로 접근이 가능하다. 먼저 들어간 데이터가 먼저 나오는 형태이다. LILO (Last In Last Out) 의 형태도 가능하다.
> - 음료수 진열대를 예시로 생각하면 되겠다.

## 사용 예시

### 일반큐 생성

```python
import queue

data_queue = queue.Queue()
```

### enqueue

```python
data_queue.put("1")
```

### dequeue

```python
# 맨 처음에 넣은 값을 리턴해주고 해당 요소를 삭제한다
data_queue.get()
```

### size

```python
data_queue.qsize()
```

## queue 라이브러리

- Queue() - 일반적인 큐
- LifoQueue() - 나중에 입력된 데이터가 먼저 나오는 구조 (스택 구조)
- PriorityQueue() - 우선 순위 큐, 우선 순위가 높은 큐가 먼저 나온다. 데이터 삽입 시, put(('우선순위', '값'))의 형태로 저장한다.
