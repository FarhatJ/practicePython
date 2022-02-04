#Demontrating Queue in Python using List

queue = []

#adding element to the queue
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
print(queue)


#delete elelment from queue

print("Elements dequeued from the queue\n")
print(queue.pop(1))
print(queue)
#print(queue.pop(0))
#print(queue)


# queue using collections deque 
from collections import deque

print("\n\nImplementing Queue using Collections deque: \n")
q = deque()

#add elements to queue

q.append("e")
q.append("f")
q.append("g")
q.append("h")
print(q)

print("Elelments dequeued from the Queue\n")
print(q.popleft())
print(q)
print(q.popleft())
print(q)

#Implementing que using queue.Queue
print("\n\nImplementing queue using queue.Queue:\n")
from queue import Queue
