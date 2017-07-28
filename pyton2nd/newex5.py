import random

def take_2_list():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	c = []
	d = random.sample(range(165), 45)		#random list
	e = random.sample(range(267), 57)
	#check if elements from a list are in other list
	for x in d:
		if x in e:
			if x not in c:
				c.append(x)
	print c

			


take_2_list()