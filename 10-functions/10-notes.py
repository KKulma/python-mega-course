# functions with multiple arguments

def my_func(arg1: str, arg2: str):
    return arg1 + arg2

# keyword (positional) arguments
print(my_func("my", "life"))


# non-keyword (non-positional) arguments
print(my_func(arg2="my", arg1="life"))


# default parameters
def my_func2(arg1: str, arg2: str, arg3="!"):
    return arg1 + arg2 + arg3

print(my_func2("my", "life"))


### functions with an arbitrary number of non-keyword arguments
# e.g. print()
# functions with a fixed number of arguments:
obj = "character"
len(obj) # always 1
isinstance(obj, str) #always 2

# define a function that calculates a mean of all the numbers passed as an input (however many!)

def my_mean_test(*args):
    return args

print(my_mean_test(1,2,3,4,5)) # return a TUPLE!


def my_mean(*args):
    return sum(args)/len(args)

print(my_mean(10,20,30,40))


### indefinite number of strings processed

def mystrings(*args):
    strings = list(args)
    result =[str(string).upper() for string in strings]
    result.sort()
    return result

print(mystrings("zebra", 'monkey', 'alpaca'))

# even better!
def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)


### functions with an arbittrary number of KEYWORD arguments

def mymean(**kwargs):
    return kwargs

print(mymean(a=1, bb = "string")) # we get a dictionary



#### indefinite number of keword arguments exercise
# predefined function, objective: make the result add up to 9,, doh
def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a = 4, b = 5))