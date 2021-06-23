def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


n = int(input())


for i in range(n):
    parent = dict()
    number = dict()

    f = int(input())
    for j in range(f):
        f1, f2 = input().split()

        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1
        union(f1, f2)
        print(number[find(f1)])


# 시간 초과
# for i in range(n):
#     f = int(input())
#     for j in range(f):
#         f1, f2 = input().split()
#         newNetwork[j] = {f1, f2}
#     network = network.union(newNetwork[0])
#     print('2')
#     for k in range(1, len(newNetwork)):
#         union = network.union(newNetwork[k])
#         if len(union) < len(network) + len(newNetwork[k]):
#             print(len(union))
#         elif len(union) == len(network) + len(newNetwork[k]):
#             print(len(newNetwork[k]))
#         network = union
#     network = set()
#     newNetwork = {}

# print(network)

# print(newNetwork)
