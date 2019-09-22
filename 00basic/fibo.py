def fib(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n.
    >>> fib(2000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
    >>> f = fib
    >>> f(100)
    0 1 1 2 3 5 8 13 21 34 55 89 
    >>> print(fib(0))
    <BLANKLINE>
    None
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n.
    >>> f100 = fib2(100) # call it
    >>> f100             # write the result
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
