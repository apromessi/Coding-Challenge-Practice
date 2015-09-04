# 1. How to find missing number in integer array of 1 to 100?

def find_missing(list1):
	correct_total = 0
	for num in range(1, 101):
		correct_total += num
	list1_total = 0
	for num in list1:
		list1_total += num
	missing_num = correct_total - list1_total
	return missing_num

# notes: assumes there's only one missing number, and all others fall between
# 1 and 100, and there are no duplicates

# 3. How to check if array contains a number in Java?

# python built in:
def find_num_py(list1, num):
	if num in list1:
		return True

# if sequential:
def find_num_seq(list1, num):

 	while list1:
 		if len(list1) == 1:
			if list1[0] == num:
				return True
			else:
				return False
		else:
			mid = len(list1)/2
			if num == list1[mid]:
				return True
			elif num < list1[mid]:
				list1 = list1[:mid]
			elif num > list1[mid]:
				list1 = list1[mid:]
	else:
		return False

# 5. How to find all pairs on integer array whose sum is equal to given number?

def find_pairs(list1, num):
	pairs = []
	for n in list1:
		if (num-n) in list1:
			pairs.append((n, num-n))
