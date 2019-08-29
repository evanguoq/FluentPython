# doctest.ellipsis.py

class MyClass:
    pass

def unpredictable(obj):
    """Return a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]

    """
    return [obj]
