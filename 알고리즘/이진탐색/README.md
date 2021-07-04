# Binary Search

## 설명

- 이진 탐색이란, 정렬된 데이터 리스트 중에서 원하는 값을 찾고자 하는 경우에 사용된다.
- 데이터 리스트의 중간 값을 기준으로 중간 값보다 찾고자 하는 데이터가 크다면 데이터 리스트의 중간 값을 기준으로 오른쪽을 탐색, 아니라면 왼쪽을 탐색한다.

## 분할 정복 알고리즘과 이진 탐색

- 분할 정복 알고리즘 (Divide and Conquer)
  - Divide: 문제를 하나 또는 둘 이상으로 나눈다.
  - Conquer: 나눠진 문제가 충분히 작고, 해결이 가능하다면 해결하고, 그렇지 않다면 다시 나눈다.
- 이진 탐색
  - Divide: 리스트를 두 개의 서브 리스트로 나눈다.
  - Conquer:
    - findData > 중간값 -> 우측에서 탐색
    - findData < 중간값 -> 좌측에서 탐색

## 방법

> [1, 2, 4, 6, 8] 의 데이터에서 6을 찾고자 하는 경우 <br/>
>
> 1. mid = 2, dataList[mid] = 4, findData = 6 -> 우측 탐색
> 2. dataList = [4, 6, 8], mid = 1, dataList[mid] = 6, findData = 6 -> 탐색 종료

## 시간 복잡도

- 길이가 n인 리스트를 절반씩 나누어 1이 될 때까지 비교연산을 진행한다.
  - n x 1/2 x 1/2 x 1/2 ... = 1
  - n x (1/2)<sup>k</sup> = 1
  - n = 2<sup>k</sup> = log<sub>2</sub><sup>n</sup> -> log<sub>2</sub><sup>n</sup> = k
  - O(log<sub>2</sub><sup>n</sup>)
