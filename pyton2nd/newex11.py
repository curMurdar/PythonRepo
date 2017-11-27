def prime_numbers(a):
	d = []
	c = int(a)
	divisors = range(2 , c-1)
	for x in divisors:
		if int(c % x) == 0:
			d.append(x)
			if len(d) != 0:
				b = 'Nu este prim'
				break
		else:
			b = 'Este prim'

	print b				

prime_numbers(raw_input(">"))
