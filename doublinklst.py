# Doubly Linked List

# Node class
class Node:
	def __init__(self, data, prev = None, next = None):
		self.data = data
		self.next = next
		self.prev = prev

class DLL(object):
	def __init__(self):
		self.head = None
	
	def printlst(self):
		node = self.head
		while node:
			print (node.data, end = "<->")
			node = node.next

		print(None)

	def deleteNode(self, val):
		tmp = self.head
		while tmp is not None:
			if tmp.data == val:
				if tmp.prev is not None:
					tmp.prev.next = tmp.next
					tmp.next.prev = tmp.prev

				else:
					self.head = tmp.next
					tmp.next.prev = None

			tmp = tmp.next


	def insertFront(self, val):
		node1 = Node(val)

		node1.next = self.head

		if self.head is not None:
			self.head.prev = node1

		self.head = node1

	def nodeAfter(self, node1, val):
		newNode = Node(val)

		if node1 is None:
			return

		newNode.next = node1.next

		node1.next = newNode

		newNode.prev = node1

		# want to change the previous of the newNode's next to newNode
		if newNode.next is not None:
			newNode.next.prev = newNode

	def nodeEnd(self, val):
		node1 = Node(val)
		last = self.head

		node1.next = None # next of last node is Null

		if self.head is None:
			node1.prev = None
			self.head = node1
			return

		while last.next is not None:
			last = last.next

		last.next = node1
		node1.prev = last


if __name__ == '__main__':
	dll = DLL()

	dll.insertFront(4)
	dll.insertFront(5)
	dll.nodeEnd(3)
	dll.nodeAfter(dll.head.next, 2)

	dll.printlst()

	dll.deleteNode(4)

	print ('\nAfter deletion:\n')

	dll.printlst()