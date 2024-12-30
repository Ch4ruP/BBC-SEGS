class Hand:
    def __init__(self):
        self.cards = []

    # Hand changes through a game
    # Initialise - each player gains two cards, these should be added to their hand
    # Player chooses to 'hit' - that player is given another card to add to their hand
    def add_card(self, card):
        self.cards.append(card)