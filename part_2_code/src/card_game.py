### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:
  def __init__(self):
    self.cards = []


  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1.value
    else: 
      return card2.value
  

  def cards_total(self, cards):
    total = 0
    for card in cards:
      total += card.value
      
    return "You have a total of " + str(total)