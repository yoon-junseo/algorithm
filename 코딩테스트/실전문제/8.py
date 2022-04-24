import sys
import heapq 
input = sys.stdin.readline

data = input().rstrip()
answer = []
num = 0

for i in range(len(data)):
    if data[i].isalpha() == True:
        answer.append(data[i])
    else:
        num += int(data[i])

alpha = sorted(answer)
alpha = ''.join(alpha)
alpha += str(num)
print(alpha)