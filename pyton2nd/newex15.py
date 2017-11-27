def backwords(words):
	words_array = words.split()
	words_array_back = []
	phrase = ""
	for i in words_array[::-1]:
		words_array_back.append(i)

	phrase = " ".join(words_array_back)
	print phrase

backwords(raw_input("Your input here> "))

