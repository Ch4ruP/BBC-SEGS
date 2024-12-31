class Hand:
    def __init__(self):
        self.cards = []
        self.bust = False
        self.lowestValue = 0 # for checking if the hand has gone bust (using low aces)

    # Hand changes through a game
    # Initialise - each player gains two cards, these should be added to their hand
    # Player chooses to 'hit' - that player is given another card to add to their hand
    # A player's total hand value increases each time a card is added
    def add_card(self, card):
        self.cards.append(card)
        if card == 'J' or card == 'Q' or card == 'K': # if face card, then add 10
            self.lowestValue += 10
        elif card == 'A': # if Ace, then add 1 (as finding the lowest value of the hand)
            self.lowestValue += 1
        else:   #if number, then add the value of that card
            self.lowestValue += card

    #Return the lowest value of the hand
    def get_lowest_value(self):
        return self.lowestValue
        
        