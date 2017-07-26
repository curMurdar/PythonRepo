print "Let's practice.."

print "First of all, we need to learn how to escape this shit\'s. Also with \\ and \ttab shit."

five = (10-5+5+5)/3

print five


def secret_formula(started):
	jelly_beans = started * 1500
	jars = jelly_beans/1000
	crates = jars/10
	return crates, jars, jelly_beans

start_point = 10000

crates, jars, beans =  secret_formula(start_point)

print "Starting with %r we have %r crates, %r jars and %r beans." % (start_point, crates, jars, beans)

print "Or, by this way, we have %r crates, %r jars and %r beans." % secret_formula(start_point)
