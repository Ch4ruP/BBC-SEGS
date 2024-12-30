import unittest
from src.gameplay import Gameplay


class GameplayTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.gameplay = Gameplay()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_init_players(self): # this tests the initial number of players is 0
        number_of_players_init = len(self.gameplay.players)
        self.assertEqual(number_of_players_init,0)
    def test_adding_players(self):  # this tests the playGame function creates a dict with the appropriate number of players
        self.gameplay.playGame(4)
        number_of_players = len(self.gameplay.players)
        self.assertEqual(number_of_players, 4)
    
    
if __name__ == '__main__':
    unittest.main()
