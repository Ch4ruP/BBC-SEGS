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
    
    def test_start_lowestVal(self): # this tests that the lowest value starts at 0
        self.assertEqual(self.hand.lowestValue,0)
    
    def test_lowestVal(self): # this tests that if a player has an ace, it will use 1 to calculate the lowest value (not 11)
        self.hand.add_card(10)
        self.hand.add_card('A')
        self.assertEqual(self.hand.lowestValue,11)
        self.assertEqual(self.hand.bust,False)
    

if __name__ == '__main__':
    unittest.main()
