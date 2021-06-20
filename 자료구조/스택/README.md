# Stack

## 설명

> - LIFO (Last In, First Out) 구조로 가장 마지막에 들어간 데이터가 가장 먼저 나온다.
> - 데이터 입.출입 관리를 한쪽 방향에서만 한다.
> - 웹 브라우저의 히스토리, 파일에서 함수 호출을 관리할 때 사용된다.

## 사용 예시

```python
stack_list = list()
stack_list.append(data) # push 역할
stack_list.pop() # pop
```

## Stack 라이브러리

보통 덱 라이브러리를 사용한다.

```python
from collections import deque

dq = deque() # 덱 생성
dq.append() # 덱의 가장 오른쪽에 원소 삽입
dq.popleft() # 가장 왼쪽 원소 반환
dq.appendleft # 덱의 가장 왼쪽에 원소 삽입
dq.pop() # 가장 오른쪽 원소 반환
dq.clear() # 모든 원소 제거
dq.copy() # 덱 복사
dq.count(x) # x와 같은 원소의 개수를 계산
```
