### objective: divide all the elements of the list by 10

# classical approach
from typing import Union

temps = [1234, 5678, 9087, 54321]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)


# list comprehension

new_temps = [temp/10 for temp in temps]
print(new_temps)


# with if conditional

temps = [1234, 5678, 9087, 54321, -9999, -18246]

new_temps = [temp/10 for temp in temps if temp > 0]
print(new_temps)

# return only integers
input = [99, 'no data', 95, 94, 'no data']

def my_func(input):
    result = [ele for ele in input if isinstance(ele, int)]
    return result

print(my_func(input))

# return only positive numbers

input = [-99, 5 , -95, -94, 'no data']

def my_func(input):
    result = [ele for ele in input if (isinstance(ele, int) and ele > 0)]
    return result

print(my_func(input))


### if else conditional

input = [-99, 5 , -95, -94, 'no data']

def my_func(input):
    result = [ele if (isinstance(ele, int) and ele > 0) else 0 for ele in input]
    return result

print(my_func(input))


# zeros instead

def my_func(input):
    result = [ele if isinstance(ele, int) else 0 for ele in input]
    return result


# convert and sum up

input = ["1.1", "2.2", "3.3", "4.4"]
result = [float(ele) for ele in input if isinstance(ele, str)]
print(sum(result))

def new_func(input):
    result = [float(ele) for ele in input if isinstance(ele, str)]
    return sum(result)


# def my_func


