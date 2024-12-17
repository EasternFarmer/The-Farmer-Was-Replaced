def better_min(items):
	numitems = []
	for item in items:
		numitems.append(num_items(item))
	index = 0
	min = 9999999999999999999999999999999
	for i in range(len(items)):
		if numitems[i] < min:
			index = i
			min = numitems[i]
	return index