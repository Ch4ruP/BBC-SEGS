class Gameplay:
    def __init__(self):
        self.currDeck = Deck()

# Initialise the game with a given number of players, by shuffling the deck and giving each player two cards
    def initGame(self,noPlayers):
        # shuffle deck
        # deal 2 cards to each player (for loop)

# If a player chooses to 'hit' (recursive function)
    def hit(self):
        # draw a card from the deck
        # add the card to the player's hand
        # check if the player has busted (value > 21)
        # if busted, end the player's turn
        # else, ask the player if they want to 'hit' or 'stand'

# If a player chooses to stand
    def stand(self):
        # end the player's turn

# Gameplay
    def playGame(self,noPlayers):
        # create the given number of players (for loop)
        # initialise game
        # for each player, ask whether they want to hit or stand
        # check which player has the highest value without going bust
            #award that player the pot