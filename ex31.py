print "Choose the way, 1 is for good, 2 is for evil"

way = raw_input(">")

if way == "1":
	print """
	There is a giant dragoon over there, what you do?
	1. Poke the dragoon.
	2. Stab his eye.
	"""
	dragoon = raw_input(">")

	if dragoon == "1":
		print "The beast eats your arm"
	elif dragoon == "2":
		print "The beast eats your face"
	else :
		print "You made the right decision to %r." % dragoon

elif way == "2":
	print "You went into abyss"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input(">")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
   	else :
   		print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
	print "What's wrong with u man?"

