import queue

data = queue.Queue()
data.put(1)
data.put(2)
data.put(3)

print(data.qsize())

print(data.get())

print(data.qsize())
