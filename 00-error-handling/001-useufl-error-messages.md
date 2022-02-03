> Not part of the course!
> Based on [Merely Useful](https://merely-useful.tech/py-rse/errors.html)

# USEFUL ERROR MESSAGES

1. Tell the user what they did, not what the program did. Putting it another way, the message shouldn’t state the effect of the error, it should state the cause.

2. Be spatially correct, i.e., point at the actual location of the error. Few things are as frustrating as being pointed at line 28 when the problem is really on line 35.

3. Be as specific as possible without being or seeming wrong from a user’s point of view. For example, “file not found” is very different from “don’t have permissions to open file” or “file is empty.”

4. Write for your audience’s level of understanding. For example, error messages should never use programming terms more advanced than those you would use to describe the code to the user.

5. Do not blame the user, and do not use words like fatal, illegal, etc. The former can be frustrating—in many cases, “user error” actually isn’t—and the latter can make people worry that the program has damaged their data, their computer, or their reputation.

6. Do not try to make the computer sound like a human being. In particular, avoid humor: very few jokes are funny on the dozenth re-telling, and most users are going to see error messages at least that often.

7. Use a consistent vocabulary. This rule can be hard to enforce when error messages are written by several different people, but putting them all in one module makes review easier.


Regarding point 7, A better approach is to put all the error messages in a dictionary:

```python
ERRORS = {
    'not_csv_suffix' : '{fname}: File must end in .csv',
    'config_corrupted' : '{config_name} corrupted',
    # ...more error messages...
    }
```

and then only use messages from that dictionary:
```python
if fname[-4:] != '.csv':
    raise OSError(ERRORS['not_csv_suffix'].format(fname=fname))
```

Doing this makes it much easier to ensure that messages are consistent. It also makes it much easier to give messages in the user’s preferred language:

## Testing error handling 

If we want to check that a function called func raises an ExpectedError exception, we can use the following template for a unit test:

```python
#...set up fixture...
try:
    actual = func(fixture)
    assert False, 'Expected function to raise exception'
except ExpectedError as error:
    pass
except Exception as error:
    assert False, 'Function raised the wrong exception'
```

or in `pytest`:

```python
import pytest
#...set up fixture...
with pytest.raises(ExpectedError):
    actual = func(fixture)
```

This template has three cases:

1. If the call to func returns a value without throwing an exception then something has gone wrong, so we assert False (which always fails).
2. If func raises the error it’s supposed to, then we go into the first except branch without triggering the assert immediately below the function call. The code in this except branch could check that the exception contains the right error message, but in this case it does nothing (which in Python is written pass).
3. Finally, if the function raises the wrong kind of exception we also assert False. Checking this case might seem overly cautious, but if the function raises the wrong kind of exception, users could easily fail to catch it.