# 투포인터 알고리즘

- 수열에서 특정한 합을 가지는 부분 연속 수열을 구하는 경우에 사용한다.

## 구현 방법

1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
2. 현재 부분합이 M과 같다면 카운트한다.
3. 현재 부분합이 M보다 작으면 end를 1만큼 증가시킨다.
4. 현재 부분합이 M보다 크거나 같으면 start를 1만큼 증가시킨다.
5. 모든 경우를 확인할 때까지 2번부터 4번을 반복한다.

```python
n = 5
m = 5
data = [1, 2, 3, 2, 5]

cnt = int(0)
sum = int(0)
end = int(0)

for start in range(n):
    while sum < m and end < n:
        sum += data[end]
        end += 1
    if sum == m:
        cnt += 1
    sum -= data[start] # 시작점을 늘려주기 때문에 현재 data[start] 값을 제거해야 한다.

print(cnt)
```

## 관련 문제

[부분합](https://www.acmicpc.net/problem/1806)
