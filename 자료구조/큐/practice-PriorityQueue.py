import queue

data = queue.PriorityQueue()

data.put((10, "10"))  # 우선순위, 값
data.put((5, "5"))
data.put((1, "1"))

print(data.qsize())

print(data.get())
print(data.get())
