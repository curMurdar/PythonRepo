import random

def rock_paper_scissors(user_choice):
	random_number = random.uniform(0, 1)
	if random_number <= 0.33:
		computer_choice = "Rock"
	elif 0.33 < random_number <= 0.66:
		computer_choice = "Scissors"
	else: 
		computer_choice = "Paper"

	if computer_choice == "Rock":
		if user_choice == "Rock":
			print computer_choice
			print "Tie"
		elif user_choice == "Paper":
			print computer_choice
			print "You win!"
		elif user_choice == "Scissors":
			print computer_choice
			print "You loose"
		else:
			print "What the fuck man?"

	elif computer_choice == "Scissors":
		if user_choice == "Rock":
			print computer_choice
			print "You win!"
		elif user_choice == "Paper":
			print computer_choice
			print "You loose"
		elif user_choice == "Scissors":
			print computer_choice
			print "Tie!"
		else:
			print "what is wrong with u?"

	else:
		if user_choice == "Rock":
			print computer_choice
			print "You loose"
		elif user_choice == "Scissors":
			print computer_choice
			print "You win"
		elif user_choice == "Paper":
			print computer_choice
			print "Tie!"
		else:
			print "You crazy man.."

rock_paper_scissors(raw_input("Rock, paper or Scissors (Type with big letter at start) "))

play_again = raw_input("Wanna play again ")

while play_again == "Yes":
	rock_paper_scissors(raw_input("Rock, paper or Scissors (Type with big letter at start) "))
	play_again = raw_input("Again? ")



