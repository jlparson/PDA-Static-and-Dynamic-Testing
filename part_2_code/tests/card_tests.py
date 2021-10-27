import unittest

from src.card import Card

class TestCard(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Club", 8)
        self.card2 = Card("Diamond", 1)
    
    # @unittest.skip("delete this line to run the test")
    def test_check_for_ace_true(self):
        result = self.card2.check_for_ace()
        self.assertEqual(True, result)

    # @unittest.skip("delete this line to run the test")
    def test_check_for_ace_false(self):
        result = self.card1.check_for_ace()
        self.assertEqual(False, result)