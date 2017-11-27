list_one = [1, 1, 2, 3, 8, 4, 5, 5, 6, 7, 123, 1234, 123, 1234]

def no_duplicates_1(list1):
	list_results = []

	for i in list1:
		if i not in list_results:
			list_results.append(i)

	print list_results

no_duplicates_1(list_one)

def no_duplicates_2(list2):
	set_results = set(list_one)
	set_results = list(set_results)
	return set_results

print no_duplicates_2(list_one)	