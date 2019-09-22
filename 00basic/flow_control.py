""" if Statements
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
"""

""" for Statements
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
>>> for w in words[:]: # Loop over a slice copy of the entire list
...     if (len(w) > 6:
...         words. insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
"""

""" The range() Function -- generates arithmetic progressions
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
range(5, 10)
    5, 6, 7, 8, 9
range(0, 10, 3)
    0, 3, 6, 9
range(-10, -100, -30)
    -10, -40, -70

Combining len and range is handy.
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for a in range(len(a))
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb

>>> list(range(5)))
[0, 1, 2, 3, 4]
"""

""" break and continue Statements and else Clauses on Loops
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...         print(n, 'equals', x, '*', n //x)
...         break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
"""

""" pass Statements - does nothing.
>>> while True:
...     pass # Busy-wait for keyboard interrupt (Ctrl + C)
>>> class MyEmptyClass:
...     pass
>>> def initlog(*args):
...     pass # Remember to implement this!
"""
