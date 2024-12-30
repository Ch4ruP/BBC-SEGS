from src.deck import Deck
from src.hand import Hand

class Gameplay:
    def __init__(self):
        self.currDeck = Deck()
        self.players = {}

# Initialise the deck for a given number of players, by shuffling and giving each player two cards
    def initDeck(self,noPlayers):
        # shuffle deck
        self.currDeck.shuffle()
        # deal 2 cards to each player (for loop which draws two cards from deck and assigns them to players hand - for each player)
        for x in range(noPlayers):
            firstDealtCard = self.currDeck.deal_cards()
            self.players[x].add_card(firstDealtCard)
            secondDealtCard = self.currDeck.deal_cards()
            self.players[x].add_card(secondDealtCard)
        return

# If a player chooses to 'hit' (recursive function)
    def hit(self, player):
        # draw a card from the deck
        dealtCard = self.currDeck.deal_cards()
        # add the card to the player's hand
        self.players[player].add_card(dealtCard)
        # check if the player has busted (value > 21)
        # if busted, end the player's turn, and set bust to true
        # else, ask the player if they want to 'hit' or 'stand'
        return

# If a player chooses to stand
    def stand(self):
        # end the player's turn
        return

# Gameplay
    def playGame(self,noPlayers):
        # create the given number of players (for loop)
        for x in range(noPlayers):
            self.players[x] = Hand()
        # initialise deck
        self.initDeck(noPlayers)
        # for each player, ask whether they want to hit or stand

# Check which player wins
    def checkWinner(self):
        # check which player has the highest value without going bust
            #award that player the pot