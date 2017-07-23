# Singly Linked List

# Node class 
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None # next is set as Null

	def getData(self):
		return self.data

class LL(object):
	# initialize the head
	def __init__(self):
		self.head = None
		
	def printlst(self):
		tmp = self.head
		while tmp is not None:
			print (tmp.data, end = "->")
			tmp = tmp.next

		print(None)

	# traversing list to find and delete node
	def deleteNode(self, val):
		tmp = self.head

		if tmp.data == val:
			self.head = tmp.next

			# free node
			tmp = None

			return

		while tmp is not None:
			if tmp.data == val:
				break

			prev = tmp
			tmp = tmp.next

		prev.next = tmp.next

		# free node
		tmp = None

	def insertFront(self, val):
		# create new node with val as the data
		node1 = Node(val)

		# make node1's next the head
		node1.next = self.head

		self.head = node1
		
	def nodeAfter(self, node1, val):
		newnode = Node(val)

		# Need to check if given node is null
		if node1 is None:
			return

		# set the new node's pointer to the given node's next
		newnode.next = node1.next

		# set given node pointer to new node
		node1.next = newnode

	# reference to head of the list
	def nodeEnd(self, val):
		node1 = Node(val)
		last = self.head

		if self.head is None:
			self.head = node1
			return

		while last.next is not None:
			last = last.next

		last.next = node1



if __name__ == '__main__':
	ll = LL()

	ll.insertFront(6)
	ll.nodeEnd(5)
	ll.nodeEnd(1)
	ll.nodeAfter(ll.head.next, 4)

	ll.printlst()

	ll.deleteNode(1)

	print ('\nAfter deletion:\n')

	ll.printlst()
