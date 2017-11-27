def calc_fibonacci(fib):
	res = []
	num0 = 0
	num1 = 1

	for numb in range(0, fib):
		num0, num1 = num1, num1 + num0
		res.append(num0)

	print res

calc_fibonacci(int(raw_input("How many times you would like fibonacci? > ")))