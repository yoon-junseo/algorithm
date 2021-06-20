test_cases = int(input())

for i in range(test_cases):
    n, m = list(map(int, input().split()))
    importance = list(map(int, input().split()))
    idx = list(range(len(importance)))
    idx[m] = 'find'
    count = 0

    while True:
        if importance[0] < max(importance):
            idx.append(idx[0])
            del idx[0]
            importance.append(importance[0])
            del importance[0]
        elif importance[0] == max(importance):
            if idx[0] == 'find':
                count += 1
                print(count)
                break
            else:
                del idx[0]
                del importance[0]
                count += 1
