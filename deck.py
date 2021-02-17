from card import Card


class Deck:
  '''
  Standard 52 playing card deck.
  4 Suits (Spades, Hearts, Diamonds, Clubs)
  13 Ranks (1 = Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 = Jack, 12 = Queen, 13 = King)
  '''
  def __init__(self):
    self._cards = []
    self.populate()

  def populate(self):
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
    self._cards = [Card(suit, rank) for suit in suits for rank in ranks]

  def shuffle(self):
    pass

  def deal(self):
    pass


  def showDeck(self):
    print(self._cards)




deck = Deck()
deck.showDeck()