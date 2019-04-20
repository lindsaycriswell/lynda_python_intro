#
# Example file for working with functions
#

# define a basic function
def func1():
    print("f1")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x * x * x

# function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_args(*args):
    result = 0
    for x in args:
        result = result + x
    return result



func1() #f1
print(func1()) #f1
print(func1) #None (b/c no return value) / <function func1 at 0x101c751e0>

print(func2(10, 20)) #10 20
print(cube(3)) #None / 27

print(power(2)) #2
print(power(2,3)) #8
print(power(x=3,num=2)) #8

print(multi_args(1)) #1
print(multi_args(1, 2)) #3
print(multi_args(1, 2, 3)) #6
