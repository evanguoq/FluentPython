""" Division
>>> 17 / 3 # classic division return a float
5.66666666666667
>>> 17 // 3 # floor division discard the fractional part
5
>>> 17 % 3 # remainder of the division
2
"""

""" Powers
>>> 5 ** 2 # 5 squared
25
>>> 2 ** 7 # 2 to the power of 7
128
"""

""" In interactive mode, the last printed expression is assigned
to the variale _.
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
"""

""" Strings - special character escape
>>> 'spam eggs' # single quotes
'spam eggs'
>>> 'doesn\'t' # use backslash \' to escape the single quote
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
"""

""" String - print
If you don't want characters prefaced by \ to be interpreted as
special characters, you can use raw strings by adding an r before
the first quote:
>>> print('C:\some\name') # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name') # note the r before the quote
C:\some\name

End of lines are automatically included in the string, but it is
possible to prevent this by adding a \ at the end of line.
>>> print('''\
Usage: thingy [OPTIONS]
    -h
    -H hostname
'''
"""

""" String - cancatination
>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' 'thon' # are automatically cancatenated
'Python'
>>> text = ('Put several strings within parantheses'
...         'to have them joined together.')
"""

""" String - index & slicing
>>> word = 'Python'

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

>>> word[0] # character in position 0
'P'
>>> word[5] # character in position 5
'n'
>>> word[-1] # last character
'n'
>>> word[0:2] # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[:2] + word[2:] # an omitted first index defaults to zero
...                     # an omitted second index defaults to the size of
...                     # the string being sliced
'Python'
>>> word[-2:] # characters from the second-last (included) to the end
'on'
>>> word[4:42] # out of range slice indexes are handled gracefully for slicing
'on'

Python strings cannot be changed -- they are immutable. If you need a
different string, you should create a new one:
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'

The build-in function len() returns the length of a string.
>>> s = 'ABCD'
>>> len(s)
4
"""

""" List - can be written as a list of comma-separated values(items)
between square brackets. List can be indexed and sliced as string.
>>> squares = [1, 4, 9, 16, 25]

All slice operateions return a new list containing the requested
elements. This means that the following slice returns a new (shallow)
copy of the slice.
>>> squares[:]
[1, 4, 9, 16, 25]
"""
