#make one big array of the given ones
def sum_arrays(arrays):
	result = []
	for array in arrays:
		result += (array)
	return result


#merge the arrays and sort them
def merge(arrays):
	my_merge_set = list(set(sum_arrays(arrays)))
	my_merge_set.sort()

	#This prevent data duplication
	#without it any int of the array has
	#one more
	first = {x: True for x in my_merge_set}

	#start merging the arrays
	for array in arrays:
		for number in array:
			if not first[number]:
				location = my_merge_set.index(number)
				my_merge_set.insert(location, number)
			else:
				first[number] = False
	return my_merge_set


arrays = [[1, 1, 1, 41, 9379], [1, 2, 3, 4, 5, 278]]
print(merge(arrays))

