import random
list = random.sample(range(999), 75)

def get_first_last(a):
	d = [c for c in a if a.index(c) in [0, 74]]
	print d

get_first_last(list)