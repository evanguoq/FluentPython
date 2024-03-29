"""List Comprehension

A list comprehension consists of brackets containing an expresion followed
by a for clause, then zero or more for or if clauses. The result will be a
new list resulting from evaluating the expression in the context of the for
and if clauses which follow it.
>>> [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""
