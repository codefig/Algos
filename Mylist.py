"""
 my analogy:
  Nodes : have next and data
  	 first has the next value to be none 
  	 and others have their own values 
  	 Unorderedlis: parent to inculcate all of the objects
  	 head to refer to current object 
  	 Started : 26/12/2015
  	 Last Edited: 4/ 1/ 2016
"""

# REMEMBER TO IMPLEMENT THE FOLLOWING METHODS 
# -> append 
# -> contains 
# -> pop()
# -> and some other list operation methods 

class UNode(object):
	def __init__(self, value):
		self.numvalue = value
		self.next = None

	def set_next(self, new_next):
		self.next = new_next

	def get_value(self):
		return self.value

	def set_value(self, new_value):
		self.numvalue = new_value

class UList(object):
	def __init__(self):
		self.current = None

	def add(self, item_value):
		"""
			create a temporary node and set it next
			to the current next item self.current 
			in the list 
		"""
		tempnode = UNode(item_value)
		tempnode.set_next(self.current)
		self.current = tempnode

	def size(self):
		"""
			returns the size of the Unorderedlist 
			e.g m.size()  -> 3
		"""
		value_count = 0
		current = self.current
		while current != None:
			value_count += 1
			current = current.next
		return value_count

	def is_empty(self):
		""" 
			returns True if the List is empty else returns False
		"""
		return True if self.current == None else False

	def search(self, item):
		""" 
		 		search function searches the list for the item 
		 		if found returns 'True' and items index in the list 
		 		e.g ('True', 2)
		 		e.g  ('False', 0)
		"""
		found = False
		loop_count = 0
		current = self.current
		while current != None and not found:
			loop_count += 1
			if current.numvalue == item:
				found = True
			else:				
				current = current.next
		return found

	def remove(self, item):
		""" 
			the remove method searches the list for the item
			and then unlinks it and deletes it from memory

		pseudocode:
			check if the item is the current item: i.e last added item
				get its next item 
				set its next to current item
				item has been unlinked in our list
				eg [33,55,22] -> delete 33
			else:
				search for the value
				make its previous as the last node
				get its next node 
				set the previous's next as the next node collected
		"""
		previous = None
		current = self.current
		found = False
		while not found:
			if current.numvalue == item:
				current = current.next 
			else:
				#self.current = self.current.next
				current = current.next
		return found

