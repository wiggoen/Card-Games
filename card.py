class Card:
  def __init__(self, suit, rank):
    self._suit = suit
    self._rank = rank

  def __repr__(self):  # Representation
    return self._rank + ' of ' + self._suit

  @property            # Get method for suit
  def suit(self):
    return self._suit

  @suit.setter         # Set method for suit
  def suit(self, suit):
    if suit in ['hearts', 'spades', 'diamonds', 'clubs']:
      self._suit = suit
    else:
      print('Error: Not a valid suit!')

  @property            # Get method for ranks
  def rank(self):
    return self._rank

  @rank.setter         # Set method for ranks
  def rank(self, rank):
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    if rank in ranks:
      self._rank = rank
    else:
      print('Error: Not a valid rank!')
