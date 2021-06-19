queue_list = list()


def enqueue(item):
    queue_list.append(item)


def dequeue():
    item = queue_list[0]
    del queue_list[0]
    return item


for i in range(5):
    enqueue(i)

print(queue_list)
print(dequeue())
print(dequeue())
