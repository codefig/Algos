#Problem solving with Data Structures and Algorithms
# Implementing a Deque "deck"


class Deque:
	""" 
		A Deque is dual faced linear data structure 
		rear <- [----------] -> front
	"""
	
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def add_front(self, item):
		self.items.append(item)

	def add_rear(self, item):
		self.items.insert(0, item)

	def remove_front(self):
		self.items.pop()

	def remove_rear(self):
		self.items.pop(0)

	def size(self):
		return len(self.items)