#Algorithms and Data Structures with python
#my own self designed parenthesis checker 

from Stackexample import Bstack
#import a stack that uses the beginning as top


def par_checker(userstring):
	"""
		This function is only applicable to structuring 
		parenthesis ( and ) 
		31/12/2015  after my laptop spoilt 
		so am using a desktop to do the coding 

	"""
	correct = True
	stack = Bstack()
	error = ""

	for xter in userstring :
		if xter == "(":
			#put into the stack 
			stack.push(xter)
			print(stack.get_items())
		elif xter == ")":
			try:
				stack.pop() # remove one ( from stack 
				
			except IndexError, e:
				correct = False
		else:
			correct = False
			error = "Improper character in userstring !"

	if stack.is_empty() and correct:
		print("correct")
	else:
		print("Incorrect")


	#for xters in string:
	# if xter == (	:
		# put into stack 
	  #elif xter == ) :
		#remove an item from the stack 
		# (()
		#then if stack is not empty


#need to implement the extended parenthesis checker