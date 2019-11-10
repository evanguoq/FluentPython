import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12 ,15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    # Given a test score, grade returns the corresponding letter grade
    i = bisect.bisect(breakpoints, score)
    return grades[i]

if __name__ == '__main__':
    import random

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
                    # returns an insertion point before the existing item
    else:
        bisect_fn = bisect.bisect # bisect is an alias for bisect_right
                    # returns an insertion point after the existing item

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

    scores = (33, 99, 77, 70, 89, 90, 100)
    grades = tuple(grade(score) for score in scores)
    print(','.join('%4d' % n for n in scores))
    print(grades)

    SIZE = 7

    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE *2)
        #insort keeps a sorted sequence always sorted
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)
