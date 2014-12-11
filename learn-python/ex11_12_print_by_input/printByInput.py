print("How old are you?",)
age = input()
print ("How tall are you?",)
height = input()
print("How much do you weight?",)
weight = input()

print("age=%r, height=%r, weight=%r" % (age, height, weight))


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