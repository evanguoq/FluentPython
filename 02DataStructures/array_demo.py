if __name__ == "__main__":
    from array import array
    from random import random
    floats = array('d', (random() for i in range(10**7)))
    fp = open('floats.bin' 'wb')
    floats.tofile(fp)
    fp.close()
