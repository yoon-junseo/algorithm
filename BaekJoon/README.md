## Set

> set을 사용하면 중복되는 원소를 제거하고 데이터들을 저장한다. -> 원소가 존재하는지 확인할 때 많이 사용된다.

## in / not in

> - a in b -> b에 a가 있다면 true 아니라면 false <br />
> - a not in b -> b에 a가 없다면 true, 있다면 false

## input 대용

- input 보다 속도가 빠르다.

```python
import sys
n = int(sys.stdin.readline())
```

## 유한 리스트

```python
# 아래 둘은 같은 결과를 갖는다.
dataList = [0] * 10001
dataList = [0 for i in range(10001)]
```
