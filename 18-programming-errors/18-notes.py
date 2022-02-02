# In Python we have i) syntax errors and ii) exceptions.

# Syntax errors

int 9
a = [1, 2, 3)


# Exceptions
a = 1
b = "2"
print(a+b)  # TypeError
print(c)  # NameError
print(a/0)  # ZeroDivisionError


# How to solve difficult errors?
# Google the last error message


# How to ask a good programming question?
# descriptive & reproducible + expected VS received outcome


# Handling Errors

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division is meaningless"


print(divide(1, 2))
print(divide(1, 0))
