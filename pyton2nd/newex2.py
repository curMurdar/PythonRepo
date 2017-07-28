input_string = raw_input("Type a number: ")
input_no = int(input_string)
input_if_what = raw_input("Do you want to check if the number is divided with another one?")

if input_if_what == "yes":

	input_to_check = raw_input("Type the number to check if divided to: ")
	input_to_cehck_no = int(input_to_check)

	if input_no % input_to_cehck_no == 0:
		print "The number is divisble"

	else:
		print "Nah.."

else:	
	if input_no % 2 == 0:
		if input_no % 4 == 0:
			print "The number is divided by 4"
		else:
			print "The number is even!"
	else:
		print "The number is not even"