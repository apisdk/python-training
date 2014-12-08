message_for_people = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
message_for_print = "Those who know %s and those who %s." % (binary, do_not)

print message_for_people
print message_for_print


print "I said: %r" % message_for_people
print "I said: %s" % message_for_people


blocked = False

print "blocked? %r" % blocked   # blocked? False

text_apple = "apple"
text_banana = "banana"

print text_apple + " and " + text_banana