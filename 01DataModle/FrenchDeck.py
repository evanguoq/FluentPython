import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        """
        >>> deck = FrenchDeck()
        >>> len(deck)
        52
        """
        return len(self._card)

    def __getitem__(self, position):
        """
        >>> deck = FrenchDeck()
        >>> deck[0]
        Card(rank='2', suit='spades')
        >>> deck[-1]
        Card(rank='A', suit='hearts')
        >>> deck[:3]
        [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
        >>> deck[12::13]
        [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
        >>> for card in deck: # doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='2', suit='spades')
        Card(rank='3', suit='spades')
        Card(rank='4', suit='spades')
        ...
        >>> for card in reversed(deck): #doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='A', suit='hearts')
        Card(rank='K', suit='hearts')
        Card(rank='Q', suit='hearts')
        ...
        """
        return self._card[position]

if __name__=="__main__":
    import doctest
    doctest.testmod()
    """
    >>> beer_card = Card('7', 'diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')
    """
