import sys
input = sys.stdin.readline

heights = []

for _ in range(9):
    heights.append(int(input()))

sum = sum(heights)
cnt = int(0)

for i in range(9):
    for j in range(i + 1, 9):
        if 100 == (sum - (heights[i] + heights[j])):
            num1, num2 = heights[i], heights[j]
            heights.remove(num1)
            heights.remove(num2)
            heights.sort()
            cnt = 1
            break
    if cnt == 1:
        break

print(*heights, sep='\n')