import sys
input = sys.stdin.readline

number = input().rstrip()
answer0 = 0
answer1 = 0

if number[0] == '1':
    answer0 += 1
else:
    answer1 += 1

for i in range(len(number) - 1):
    if number[i] != number[i + 1]:
        if number[i + 1] == '0':
            answer1 += 1
        else:
            answer0 += 1

print(min(answer0, answer1))