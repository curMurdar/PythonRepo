import random

def random_gen_pass(len):
	symbols = random.sample('!@#$%^&*()_+|}{":', 2)
	if len == "weak":
		length = 6
	elif len == "normal":
		length = 8
	elif len == "strong":
		length = 16
	else:
		lengh = 10

	numbers_array = map(str, random.sample(range(50), length))
	letters_array = random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], length)
	password_array = symbols + numbers_array + letters_array
	random.shuffle(password_array)
	password = "".join(password_array)

	print password

random_gen_pass(raw_input("How long? (weak, normal, strong) > "))