> Not part of the course!
> Based on [Merely Useful](https://merely-useful.tech/py-rse/errors.html)


# EXCEPTIONS 

If nothing unexpected happens inside the try block, the except block isn’t run. If something goes wrong inside the try, on the other hand, the program jumps immediately to the except

```python
for denom in [-5, 0, 5]:
    try:
        result = 1/denom
        print(f'1/{denom} == {result}')
    except:
        print(f'Cannot divide by {denom}')
```

We often want to know exactly what went wrong, so Python and other languages store information about the error in an object (which is also called an exception). We can catch an exception and inspect it as follows:

```python
for denom in [-5, 0, 5]:
    try:
        result = 1/denom
        print(f'1/{denom} == {result}')
    except Exception as error:
        print(f'{denom} has no reciprocal: {error}')
```

Python also allows us to specify what kind of exception we want to catch. For example, we can write code to handle out-of-range indexing and division by zero separately:

```python
numbers = [-5, 0, 5]
for i in [0, 1, 2, 3]:
    try:
        denom = numbers[i]
        result = 1/denom
        print(f'1/{denom} == {result}')
    except IndexError as error:
        print(f'index {i} out of range')
    except ZeroDivisionError as error:
        print(f'{denom} has no reciprocal: {error}')
```

Exceptions are organized in a hierarchy: for example, `FloatingPointError`, `OverflowError`, and `ZeroDivisionError` are all special cases of `ArithmeticError`, so an except that catches the latter will catch all three of the former, but an except that catches an `OverflowError` won’t catch a `ZeroDivisionError`. [The Python documentation](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) describes all of the built-in exception types

In practice, the ones that people handle most often are:
- `ArithmeticError`: something has gone wrong in a calculation. 
- `IndexError` and `KeyError`: something has gone wrong indexing a list or lookup something up in a dictionary.
- `OSError`: thrown when a file is not found, the program doesn’t have permission to read it, and so on.

This is how we RAISE an error:

```python
for number in [1, 0, -1]:
    try:
        if number < 0:
            raise ValueError(f'no negatives: {number}')
        print(number)
    except ValueError as error:
        print(f'exception: {error}')
```

When raising an error follow the pattern called “throw low, catch high”: write most of your code without exception handlers, since there’s nothing useful you can do in the middle of a small utility function, but put a few handlers in the uppermost functions of your program to catch and report all errors:


```python 
def sum_reciprocals(values):
    result = 0
    for v in values:
        result += 1/v
    return result

numbers = [-1, 0, 1]
try:
    one_over = sum_reciprocals(numbers)
except ArithmeticError as error:
    print(f'Error trying to sum reciprocals: {error}')
```

The “if then raise” approach is sometimes referred to as “look before you leap,” while the try/except approach obeys the old adage that “it’s easier to ask for forgiveness than permission.” The first approach is more precise, but has the shortcoming that programmers can’t anticipate everything that can go wrong when running a program, so there should always be an except somewhere to deal with unexpected cases.
The one rule we should always follow is to check for errors as early as possible so that we don’t waste the user’s time. Few things are as frustrating as being told at the end of an hour-long calculation that the program doesn’t have permission to write to an output directory. It’s a little extra work to check things like this up front, but the larger your program or the longer it runs, the more useful those checks will be.