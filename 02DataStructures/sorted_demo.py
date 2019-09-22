"""list.sort and the sorted Built-In Function

>>> fruits = ['grape', 'raspberry', 'apple', 'banana']
>>> sorted(fruits) # This produces a new list of strings sorted alphabetically.
...                # The original list is unchanged.
['apple', 'banana', 'grape', 'raspberry']
>>> sorted(fruits, reverse=True)
['raspberry', 'grape', 'banana', 'apple']
>>> sorted(fruits, key=len)
['grape', 'apple', 'banana', 'raspberry']
>>> fruits # So far, the ordering of the original fruits lis has not changed

>>> fruits.sort() # This sorts the list in place, and return None
>>> fruits
['apple', 'banana', 'grape', 'raspberry']
"""
