n = int(input())
targetList = list(map(int, input().split()))
dict = {}
for i in range(n):
    dict[targetList[i]] = '1'

m = int(input())
myList = list(map(int, input().split()))

for i in range(m):
    if dict.get(myList[i]):
        print(1)
    else:
        print(0)


# n = int(input())
# target = set(map(int, input().split()))
# m = int(input())
# myList = list(map(int, input().split()))

# for i in myList:
#     if i not in target:
#         print(0)
#     else:
#         print(1)
