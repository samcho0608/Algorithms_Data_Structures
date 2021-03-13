from queue import PriorityQueue
q = PriorityQueue()
# q.put() to enqueue
# to set your own priority
# use tuple
q.put((3,'World!'))
q.put((2,','))
q.put((1,'Hello'))

# to deque
while not q.empty():
    print(q.get()[1], end='')