# this one is like your scripts with argv

def print_two(*args):
    print("argument count = %d" % len(args))
    print(" args[0] = %r" % args[0])
    print(" args[1] = %r" % args[1])
    print(" args[2] = %r" % args[2])

    # arg1, arg2 = args
    # print("arg1: %r, arg2: %r" % (arg1, arg2))


# *args is actually pointless.
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)


# this one takes no arguments
def print_none_arguments():
    print("I got nothing.")


print_two("Zed", "Shaw", "Jack")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none_arguments()