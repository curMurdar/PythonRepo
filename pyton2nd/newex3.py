#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

def Take_all_elements(d):
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	c = []
	int_d = int(d)
	for i in a:
		if i < int_d:
			c.append(i)

	print c


Take_all_elements(raw_input(">"))