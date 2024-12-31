from src.deck import Deck
from src.gameplay import Gameplay


def play():
    gameplay = Gameplay()
    print('Hello, players!')
    gameplay.playGame(3)

if __name__ == '__main__':
    play()
