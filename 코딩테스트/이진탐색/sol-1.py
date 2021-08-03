import sys

n = sys.stdin.readline().rstrip()
array1 = list(map(int, sys.stdin.readline().rstrip().split()))
array1.sort()

m = sys.stdin.readline().rstrip()
array2 = list(map(int, sys.stdin.readline().rstrip().split()))

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


for i in range(len(array2)):
    result = binarySearch(array1, array2[i], 0, len(array1) - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')