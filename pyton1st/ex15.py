from sys import argv

script, file_name = argv
text = open(file_name)

print "Here is the file you wanna open %r" % file_name
print text.read()

print "Type the filename again:"
file_again = raw_input(">")

txt = open(file_again)

print txt.read()

text.close()
txt.close()