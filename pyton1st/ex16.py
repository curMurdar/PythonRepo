from sys import argv

script, file_name = argv

print "We are gonna to erase this file %r" % file_name
print "If you don't wanna do it, hit CTRL+C, if you do hit Return"
raw_input("?")

print "Opening the file..."
target = open(file_name, "a")

print "Deleting the file..."
#target.truncate()

print "Now, we should write smt else there..I'll ask u for 3 lines:"

line1 = raw_input(">")
line2 = raw_input(">")
line3 = raw_input(">")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.close()

target = open(file_name)

print target.read()

target.close()

