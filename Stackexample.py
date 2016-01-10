#dis code is trying to implement a stack data structure on 
#my own


#LIFO

class EStack(object):
	""" 
		THIS IS a stack data structure example where the top 
		is at the end  
	"""

	def __init__(self):
		self.cont  = []

	def push(self, item):
		self.cont.append(item)

	def peek(self):
		"""
			returns the top of the stack 
		"""
		return str(self.cont[:-1])

	def pop(self):
		return self.cont.pop()

	def size(self):
		return len(self.cont)

	def is_empty(self):
		return len(self.cont) == 0


class Bstack(object):
	""" 
		this is a stack data structure implemented 
		with the top is at the beginning and not the end
		and the base at the end 
	"""

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self,item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

	def get_items(self):
		""" this function was addded by me to understand 
			the parenthesis checker i designed 
			returns items in the list (items)
		"""
		return self.items
