import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numList = list(map(int, input().split()))

end = int(0)
sum = int(0)
answer = 1e9
cnt = int(0)
done = False

for start in range(n):
    while sum < s and end < n:
        sum += numList[end]
        end += 1
    if sum >= s:
        done = True        
        temp = end - start
        answer = min(answer, temp)
    sum -= numList[start]

if done == False:
    print(0)
else:
    print(answer)
# # start를 차례대로 증가시키며 반복
# for start in range(n):
#     # end만큼 이동시키기
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         print('w', start, end, interval_sum)
#         end += 1
#         print('after', start, end, interval_sum)
#     # 부분합이 m일 때 카운트 증가
#     if interval_sum == m:
#         count += 1
#     interval_sum -= data[start]
#     print('o', start, end, interval_sum)
 
# print(count)