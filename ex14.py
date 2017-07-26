from sys import argv
script, user_name = argv
prompt = '>'

print "Hi %s, I'm %s script" % (user_name, script)
print "I'd like to ask u some questions"

print "Do you like me %s?" % user_name
like = raw_input(prompt)

print "Where do u live?"
live = raw_input(prompt)

print "What kind of weed do you like, %s?" % user_name
weed = raw_input(prompt)

print """
Alright, u said you %r about liking me.
You live in %r, that's kind of fucked up.
And also you samde that u like %r, that's some good ass weed :).
""" % (like, live, weed)
