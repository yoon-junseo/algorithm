import queue
data = queue.LifoQueue()

data.put("1")
data.put("2")

print(data.get())
print(data.qsize())
