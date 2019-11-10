"""Various means of building a dict.

>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'one': 1, 'two': 2, 'three': 3})
>>> a == b == c == d == e
True
"""

""" dict Comprehensions

>>> DIAL_CODES = [
...     (86, 'China'),
...     (91, 'India'),
...     (1,  'United States'),
...     (81, 'Japan'),
... ]
>>> country_code = {country: code for code, country in DIAL_CODES}
>>> country_code 
{'China': 86, 'India': 91, 'United States': 1, 'Japan': 81}
>>> {code: country.upper() for country, code in country_code.items()
... if code < 85}
{1: 'UNITED STATES', 81: 'JAPAN'}
"""
