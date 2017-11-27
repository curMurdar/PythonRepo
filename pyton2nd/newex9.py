import random 
def input_from_man(str):
	number_random = random.randint(1, 9)
	if str <= number_random:
		print "Your number is lower then the PC number"
	elif str >= number_random:
		print "Your number is bigger then the PC number"
	else:
		print "You're the man"


number_or_exit = raw_input("Pick a number from 1 to 9 or type exit to quit! >")
if number_or_exit == "exit":
	print "Thank you, bye!"
else:
	number_or_exit = int(number_or_exit)
count = 1

while isinstance( number_or_exit, int ):
	input_from_man(number_or_exit)
	number_or_exit = raw_input("Pick a number from 1 to 9 or type exit to quit! >")
	if number_or_exit == "exit":
		print "You tried %s time" % count
		print "Thank you, bye!"
	else:
		number_or_exit = int(number_or_exit)
		count += 1