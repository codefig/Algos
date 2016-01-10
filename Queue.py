#Problem solving with Data Structures and Algorithms 
#python implementation of a queue 
#Queue is an abstract data Structure and linear data Structure too


class Queue:
	"""
		A Queue is a FIFO Structure , 
		enqueue -> adds item to the queue
		dequeue -> removes the first item in the queue
	"""

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

		