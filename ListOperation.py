-----------------#python data structures
#testing python data structures
#Problem solving with Algorithms and Data structures in python
# 30/12/2015


#attempting to test the Algorithms ananlysis on python list methods

def test():
	#creating a list by concatenation
	l = []
	for i in range(1000):
		l = l + [i]

def test2():
	# creating a list using the append method
	l = []
	for i in range(1000):
		l.append(i)

def test3():
	# creating a list using list comprehension
	l = [i for i in range(1000)]

def test4():
	# creating a list using the list class constructor
	l = list(range(1000))
