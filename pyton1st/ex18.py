def print_two (*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one (arg):
	arg1 = arg
	print "arg1: %r" % (arg1)

def print_smt ():
	print "Muie!"

print_two("Sugi", "Pula")
print_one("Sugi pula!")
print_smt()