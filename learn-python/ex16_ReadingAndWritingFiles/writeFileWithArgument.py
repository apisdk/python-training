from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
input("delete fileName?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. GoodBye!")
target.truncate()

line1 = input("1:")
line2 = input("2:")
line3 = input("3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()