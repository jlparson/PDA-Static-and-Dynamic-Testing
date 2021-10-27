import unittest
from src.card import Card
from src.card_game import *
import pdb

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Club", 8)
        self.card2 = Card("Diamond", 1)
        self.card3 = Card("Heart", 6)
        self.cardgame = CardGame()

    
    # @unittest.skip("delete this line to run the test")
    def test_highest_card_8_over_1(self):
        result = self.cardgame.highest_card(self.card1, self.card3)
        self.assertEqual(8, result)

    # @unittest.skip("delete this line to run the test")
    def test_card_total_is_9(self):
        cards = [self.card1, self.card2]
        result = self.cardgame.cards_total(cards)
        self.assertEqual("You have a total of 9", result)