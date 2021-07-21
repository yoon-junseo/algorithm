import sys
n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]
sum = 0

#### 
# 1번째 풀이
####
# while True:
#     for j in range(k):
#         if m == 0:
#             break
#         sum += first
#         m -= 1
#     if m == 0:
#         break
#     sum += second
#     m -= 1

#### 
# 2번째 풀이
####
sum += (first * k + second) * (m // (k + 1))

if m % (k + 1):
    for i in range(m % (k + 1)):
        sum += first

#### 
# 3번째 풀이
####
# count = int(m / (k+1)) * k
# count += m % (k+1)
# sum += (count) * first
# sum += (m-count) * second


print(sum)