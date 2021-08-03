# 이진 탐색
import sys

def binarySearch(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, end)

n, target = list(map(int, sys.stdin.readline().split()))

array = list(map(int, sys.stdin.readline().split()))

result = binarySearch(array, target, 0, n - 1)
if result == None:
    print('없음')
else:
    print(result + 1, '번째에 있다.')