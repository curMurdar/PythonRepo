def a_plaindrome_lol(str):
	reversed_lol = str[::-1]
	if reversed_lol == str:
		print "Is a plaindrome"
	else:
		print "Oh Crap.."

def a_plaindrome_for(str):
	d = []
	str_array = range(1,len(str)+1)
	for x in str_array:
		d.append(str[-x])
	
	rev = ''.join(d)
	print rev
	if rev == str:
		print "yes, it is!"
	else:
		print "Nah.."


#a_plaindrome_lol(raw_input("Enter a palindrome>"))
a_plaindrome_for(raw_input("Enter a palindrome>"))