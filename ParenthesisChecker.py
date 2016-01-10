#Problem solving with Algorithms and Data Structures
#
#Using the stack data Structures to create a parenthesis balancer
# (() () ())


from Stackexample import Bstack

def par_checker(symbol_string):
	""" 
		this function is designed to match only braces ()
		and not other parenthesis types

	"""
	s  = Bstack()
	balanced = True
	index = 0

	while index < len(symbol_string) and balanced:
		symbol  = symbol_string[index]
		if symbol == '(':
			s.push(symbol)
		else:
			#IF THE SYMBOL IS NOT (
			print(s.get_items())
			if s.is_empty():
				balanced  = False
			else:
				s.pop()

		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False


def par_checker_advanced(symbol_string):
	"""
		Extended parenthesis checker to match parenthesis like 
		'{',(, [, ])}
	"""
	
	s =  Bstack()
	balanced = True
	index = 0
	while  index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False
def matches(open, close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)

print(par_checker_advanced("{{([][])}()}"))
print(par_checker_advanced("[{()]"))
print(par_checker_advanced("{()]}"))

