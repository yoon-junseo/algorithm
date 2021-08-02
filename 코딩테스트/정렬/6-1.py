# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    idx = i
    for j in range(i + 1, len(array)):
        if array[idx] > array[j]:
            idx = j      
    array[idx], array[i] = array[i], array[idx]

print(array)