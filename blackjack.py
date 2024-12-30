from src.deck import Deck
from src.gameplay import Gameplay


def play():
    gameplay = Gameplay()
    print('Hello, potential future BBC developer!')  # execution starts here! remove this print() and add your own code.
    gameplay.playGame(3)

if __name__ == '__main__':
    play()
