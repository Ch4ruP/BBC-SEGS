import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest; this tests there are 52 cards in deck
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
    def test_card_values_aces(self): # tests that there are four aces in the deck 
        number_of_aces = self.deck.cards.count("A")
        self.assertEqual(number_of_aces, 4)
    def test_card_values_sevens(self): # tests that there are four sevens in the deck 
        number_of_sevens = self.deck.cards.count(7)
        self.assertEqual(number_of_sevens, 4)
    def test_card_values_kings(self): # tests that there are four kings in the deck 
        number_of_kings = self.deck.cards.count("K")
        self.assertEqual(number_of_kings, 4)

if __name__ == '__main__':
    unittest.main()
