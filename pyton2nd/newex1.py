from datetime import date

age = input("How old are you? >")
name = raw_input("Whats your name? >")

year_of_input = date.today().year

year_of_birth = year_of_input - age
year_of_100 = year_of_birth + 100

no_of_copies = input("How many times do you want to repeat the message?")

for i in range(no_of_copies):
	print "Dear %s you will be 100 in %s \n" %(name, year_of_100)