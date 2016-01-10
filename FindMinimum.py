
#
# Problem solving with Data structures and Algorithms
# A python function to compute the minimum number in a given list
# 12/ 28 / 2015
# - i used my desktop computer cos my laptop was bad 
# with the Errror "Sorry battery not found"
#Topic : Algorithm analysis

import time
def find_min(ulist):
	"""
		This function is linear .. O(n)
	"""
	current_num  = 0
	min_num = 0
	start_time = time.time()
	current_num = ulist[0]

	for other_nums in ulist[1:]:
		# print("Trying : " + str(other_nums) + " current min: " + str(current_num))
		if current_num <= other_nums:
			min_num = current_num
		else:
			min_num = other_nums
			current_num = other_nums
	end_time = time.time()
	print min_num
	print(end_time - start_time)


	
#trying out the function 
lista = [33,44,55,44,2,1,99,33,44,55,90,339,2444,23,4,24]
listb = list(range(10000))
# # listc = list(range(100000))
# # listd = list(range(1000000))
# # liste = list(range(10000000))
# liste = list(range(100000000))

find_min(listb)
# find_min(listc)