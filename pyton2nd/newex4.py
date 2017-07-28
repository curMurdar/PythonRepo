def divisible_number(a):
	b = []
	int_a = int(a)
	c = range(1,int_a)
	for x in c:
		if (int_a % x) == 0:
			b.append(x)

	print b

divisible_number(raw_input(">"))