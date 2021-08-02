# 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(array, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end

    # 왼쪽 값이 오른쪽보다 작을 때까지
    while left <= right:
        # 왼쪽 값이 pivot 보다 작을 때까지 and 왼쪽이 끝을 넘기전까지
        while left <= end and array[left] <= array[pivot] :
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)

quickSort(array, 0, len(array) - 1)
print(array)
        
