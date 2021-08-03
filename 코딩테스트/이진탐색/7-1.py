# 순차 탐색
import sys

def sequentialSearch(n, target, array):
    for i in range(len(array)):
        if array[i] == target:
            return i + 1

print('생성할 원소 개수를 입력하고, 한 칸 띄고 찾을 문자열 입력')
n, target = sys.stdin.readline().split()

array = []
for i in range(int(n)):
    data = input('문자열 1개: ')
    array.append(data)

print(sequentialSearch(n, target, array), '번째에 위치해있다.')