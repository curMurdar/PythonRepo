from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %r, to %r" % (from_file, to_file)

indata = open(from_file).read()

print "The input is %r long" % len(indata)

print "Does the input file exist? \n %r" % exists(from_file)

out_file = open(to_file, "a").write(indata + "\n")

print "That's it!"
