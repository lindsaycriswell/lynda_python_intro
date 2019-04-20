#
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works
f = "str0"
print(f)

# # ERROR: variables of different types cannot be combined
# but this works
print("string" + str(123))

# Global vs. local variables in functions
def some_func():
    global f
    f = "str1"
    print(f)

some_func()
# f is global
print(f)

# delete variable
del(f)
print(f)
