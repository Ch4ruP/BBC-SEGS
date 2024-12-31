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
    
    def test_closestVal(self): # this tests that if a player has an ace, the best option will be used to calculate the closest value
        self.hand.add_card(10)
        self.hand.add_card('A')
        closest_val = self.hand.get_closest_val()
        self.assertEqual(closest_val,21)
    
    def test_closestVal_two_aces(self): # this tests that if a player has two aces, the best option will be used
        self.hand.add_card(9)
        self.hand.add_card('A')
        self.hand.add_card('A')
        closest_val = self.hand.get_closest_val()
        self.assertEqual(closest_val,21)

if __name__ == '__main__':
    unittest.main()
