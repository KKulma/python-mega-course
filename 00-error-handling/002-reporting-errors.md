> Not part of the course!
> Based on [Merely Useful](https://merely-useful.tech/py-rse/errors.html)

# REPORTING ERRORS / LOGGING

A better approach is to use a [logging framework](https://merely-useful.tech/py-rse/glossary.html#logging_framework), such as Python’s [logging](https://docs.python.org/3/library/logging.html) library. This lets us leave debugging statements in our code and turn them on or off at will. It also lets us send output to any of several destinations, which is helpful when our data analysis pipeline has several stages and we are trying to figure out which one contains a bug.
In principle, logging works like this: 

```python
if LOG_LEVEL >= 0:
    print('Processing files...')
for fname in args.infiles:
    if LOG_LEVEL >= 1:
        print(f'Reading in {fname}...')
    if fname[-4:] != '.csv':
        msg = ERRORS['not_csv_suffix'].format(fname=fname)
        raise OSError(msg)
    with open(fname, 'r') as reader:
        if LOG_LEVEL >= 1:
            print(f'Computing word counts...')
        update_counts(reader, word_counts)
```

In practice, we can use `logging` package to achieve the same outcome: 

```python
import logging


logging.info('Processing files...')
for fname in args.infiles:
    logging.debug(f'Reading in {fname}...')
    if fname[-4:] != '.csv':
        msg = ERRORS['not_csv_suffix'].format(fname=fname)
        raise OSError(msg)
    with open(fname, 'r') as reader:
        logging.debug('Computing word counts...')
        update_counts(reader, word_counts)
```

A logging framework combines the if and print statements in a single function call and defines standard names for the logging levels. In order of increasing severity, the usual levels are:

- DEBUG: very detailed information used for localizing errors.
- INFO: confirmation that things are working as expected.
- WARNING: something unexpected happened, but the program will keep going.
- ERROR: something has gone badly wrong, but the program hasn’t hurt anything.
- CRITICAL: potential loss of data, security breach, etc.

You can set the logs to be saved in a file (below). Also, this code snippet shows how set the logging level using the `level` argument:

```python
import logging


logging.basicConfig(level=logging.DEBUG, filename='logging.log')

logging.debug('This is for debugging.')
logging.info('This is just for information.')
logging.warning('This is a warning.')
logging.error('Something went wrong.')
logging.critical('Something went seriously wrong.')
```

Or to be sent both, the a file and the standard error:

```python
import logging


logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("logging.log"),
        logging.StreamHandler()])

logging.debug('This is for debugging.')
```