# Stack and Queue Implementations Refresher

class Stack:
	def __init__(self):
		self.el = []

	def isEmpty(self):
		return self.el == []

	def size(self):
		return len(self.el)

	def push(self, item):
		self.el.append(item)

	def pop(self):
		return self.el.pop()

	def __str__(self):
		return str(self.el)


class Queue:
	def __init__(self):
		self.el = []

	def isEmpty(self):
		return self.el == []

	def size(self):
		return len(self.el)

	def enqueue(self, item):
		self.el.insert(0, item)

	def dequeue(self):
		return self.el.pop()

	def __str__(self):
		return str(self.el)

print('\nStack: ')
S = Stack()
S.push(4)
S.push(3)
S.push(1)
print(S); print(S.isEmpty()) 
print(S.pop()); print(S.size())

print('\nQueue: ')

Q = Queue()
Q.enqueue(5)
Q.enqueue(8)
Q.enqueue(9)
print(Q); print(Q.dequeue()); print(Q.size())
