def add(a, b):
	return a + b

def substr(a, b):
	return a-b

def divide (a, b):
	return a/b

age = add(15, 9)
height = substr(210, 20)
iq = divide (50, 2)

print "Your age is %r, your height is %r and your iq is %r" % (age, height, iq)