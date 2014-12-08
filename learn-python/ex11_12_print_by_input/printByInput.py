print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "age=%r, height=%r, weight=%r" % (age, height, weight)


# result :
# How old are you? 30
# How tall are you? 180
# How much do you weight? 180
# age='30', height='180', weight='180'

# if remove ',' from question message :
# How old are you?
# 30
# How tall are you?
# 180
# How much do you weight?
# 180
# age='30', height='180', weight='180'
#