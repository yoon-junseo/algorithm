# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min = array[i]
    idx = 0
    swap = False
    for j in range(i+1, len(array)):
        if min > array[j]:
            min = array[j]
            idx = j
            swap = True
    if swap == True:
        array[i], array[idx] = array[idx], array[i]
        
print(array)