""" script to demo bad formatting fixed by an action """


def my_function():
    # the formatter doesn't like single-quotes
    a = 'please format me'

    # the formatter doesn't like long lines > 120 chars
    long_line = {'pretty_long_key_name': 'this is a very very very very very very vvery very very very very very very very very long value'}
    return 0
