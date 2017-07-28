_name = "Tavy"
_age = 24
_height = 190
_weight = 95
_eyes = "brown"
_hair = "black"
convert_cm_to_inch = _height*1/2.54

print "Let's talk about %s." % _name
print "I'am %s years old." % _age
print "My eyes are %s and my hair is %s and my height is %r" % (_eyes, _hair, _height)
print "If i add %d, and %d and %d, i got %d"  % (_age, _height, _weight, _age+_height+_weight)
print "Converted", convert_cm_to_inch