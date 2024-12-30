import random

class Deck:
    def __init__(self):
        self.cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']*4

    # Initialise / Hit - when a player is given a card, it should be removed from the deck and returned from the function
    def deal_cards(self):
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)
