"""Formatted string literals

>>> year = 2018
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2018 Referendum'
"""

""" str.format()

>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
' 42372654 YES votes 49.67%'
