import unittest
from src.gameplay import Gameplay
from src.hand import Hand


class GameplayTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.gameplay = Gameplay()
        self.hand = Hand()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_init_players(self): # this tests the initial number of players is 0
        number_of_players_init = len(self.gameplay.players)
        self.assertEqual(number_of_players_init,0)
    
    def test_adding_players(self):  # this tests the playGame function creates a dict with the appropriate number of players
        self.gameplay.playGame(5)
        number_of_players = len(self.gameplay.players)
        self.assertEqual(number_of_players, 5)
    
    def test_hit(self): # this tests whether a players number of cards increases to 3 when the hit function is executed
        self.gameplay.playGame(5)
        self.gameplay.hit(self.gameplay.players[0])
        player_num_cards = len(self.gameplay.players[0].cards)
        self.assertEqual(player_num_cards, 3)
    
    def test_going_bust(self): # this tests that if a player has 21 and gets another card they will go bust
        self.hand.add_card(10)
        self.hand.add_card(11)
        self.assertEqual(self.hand.bust,False)
        self.gameplay.hit(self.hand)
        self.assertEqual(self.hand.bust,True)
    
    
if __name__ == '__main__':
    unittest.main()
