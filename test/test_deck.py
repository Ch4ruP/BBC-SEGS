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

    def test_pop_func(self): # tests that a card is removed and its value returned when dealing
        returned_card = self.deck.deal_cards()
        self.assertIn(returned_card, ('A',2,3,4,5,6,7,8,9,10,'J','Q','K'))
        number_of_cards_pop = len(self.deck.cards)
        self.assertEqual(number_of_cards_pop,51)
    
    def test_shuffle_func(self): # tests that the deck is the correct length when shuffled (an alternative would be to use a seed
    # to ensure it correctly shuffles each time but I think this is unnecessary as I'm using a built-in python method to shuffle)
        self.deck.shuffle()
        number_of_cards_shuffle = len(self.deck.cards)
        self.assertEqual(number_of_cards_shuffle, 52)

if __name__ == '__main__':
    unittest.main()
