import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    number = int(input())
    cnt = int(0)

    while number > 0:      
        if number % 2 == 1:
            print(cnt, end=' ')
        
        number = number // 2
        cnt += 1
    print()