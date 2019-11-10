""" A python array is as lean as as a C array.

If the list will only contain numbers, an array.array is more
efficient than a list: it supports all mutable sequence
operations, and additional method for fast loading and
saving such as .frombytes and .tofile.
"""

if __name__ == "__main__":
    from array import array
    from random import random
    floats = array('d', (random() for i in range(10**7)))
    fp = open('floats.bin' 'wb')
    floats.tofile(fp)
    fp.close()
