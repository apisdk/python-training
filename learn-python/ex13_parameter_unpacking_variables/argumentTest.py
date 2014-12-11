from sys import argv

#script parameter : first second third

#unpacking from argument variables
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# result:
#
# The script is called: /python/python-training/learn-python/ex13_parameter_unpacking_variables/argumentTest.py
# Your first variable is: first
# Your second variable is: second
# Your third variable is: third


# error occur messages
# 1. ValueError: too many values to unpack
# 2. ValueError: need more than 3 values to unpack
