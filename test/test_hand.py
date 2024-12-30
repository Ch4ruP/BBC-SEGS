import unittest
from src.hand import Hand


class HandTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.hand = Hand()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_init_number_of_cards(self):  # this tests there are no cards in hand to start
        number_of_cards = len(self.hand.cards)
        self.assertEqual(number_of_cards, 0)
    def test_cards_after_adding(self): # this tests cards can be added to the hand
        self.hand.add_card('A')
        number_of_cards = len(self.hand.cards)
        self.assertEqual(number_of_cards, 1)
    
if __name__ == '__main__':
    unittest.main()
