""" List Comprehesions (listcomps)

List comprehensions is an explicit way to build a new list.

>>> symbols = 'ABCDXYZ'
>>> codes = [ord(symbol) for symbol in symbols]
>>> codes
[65, 66, 67, 68, 88, 89, 90]
>>> largeCodes = [ord(s) for s in symbols if ord(s) > 80]
>>> largeCodes
[88, 89, 90]

>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> tshirts = [(color, size) for color in colors
...                          for size in sizes]
>>> tshirts
[('black', 'S'),
 ('black', 'M'),
 ('black', 'L'),
 ('white', 'S'),
 ('white', 'M'),
 ('white', 'L')]
"""

""" Generator Expressions (Genexps)

Genexps is used to inilialise tuples, arrays, and other type of sequences.
A genexp saves memory because it yields items one by one using the iterator
protocol instead of building a whole list just to feed another constructor.

>>> symbols = 'ABCDXYZ'
>>> tuple(ord(symbol) for symbol in symbols)
(65, 66, 67, 68, 88, 89, 90)
>>> import array
>>> array.array('I', (ord(symbol) for symbol in symbols))
array('I', [65, 66, 67, 68, 88, 89, 90])

>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
...     print(tshirt)
...
black S
black M
black L
white S
white M
white L
"""

""" Tuple as Records

>>> lax_coordinates = (33.9425, -118.408056)
>>> city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) #unpacking
>>> traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
...     ('ESP', 'XDA205856')]
>>> for passport in sorted(traveler_ids):
...     print('%s/%s' % passport)
...
BRA/CE342567
ESP/XDA205856
USA/31195855

A dummy variable like _ is used as placeholder
>>> for country, _ in traveler_ids: # unpacking
...     print(country)
...
USA
BRA
ESP

Swap the values of variabls without using a temporary variable. 
>>> b, a = a, b

>>> t = (20, 8)
>>> quotient, remainder = divmod(*t) # unpacking
>>> quotient, remainder
(2, 4)

Using * to grab excess items as a list
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
>>> a, b, *rest = range(2)
>>> a, b, rest
(0, 1, [])
>>> a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
"""

""" namedtuple -- enhanced tuple with a class name and field names

>>> from collections import namedtuple
>>> City = namedtuple('City', 'name country population coordinates')
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
>>> tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
>>> tokyo.population
36.933
>>> tokyo.coordinates
(35.689722, 139.691667)
"""

""" Slicing

>>> l = [10, 20, 30, 40, 50]
>>> l[:2]
[10, 20]
>>> l[2:]
[30, 40, 50]

s[a:b:c] can be used to specify a stride or step c.
>>> s = 'bicycle'
>>> s[::3]
'bye'
>>> s[::-1]
'elcycib'
"""

