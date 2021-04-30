import random

class Card():
    
    def __init__(self, suit, rank):

        self.suit = suit

        COURT = ["J", "Q", "K"]
        self.rank = rank
        if rank > 10:
            self.face = COURT[rank - 11]
        elif rank == 1:
            self.face = "A"
        else:
            self.face = None
        
    def __str__(self):
        if not self.face:
            return "%s%s" % (self.suit, str(self.rank))
        else:
            return "%s%s" % (self.suit, self.face)

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


class Deck():
    
    def __init__(self):
        self.cards = []
        for suit in ["S", "H", "C", "D"]:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # td: shuffle
    
    # td: hand out



class Hand():
    
    def __init__(self, cards):
        self.cards = []
        self.cards += cards
    
    def get_aces(self):
        aces = 0
        for card in self.cards:
            if card.face == "A":
                aces += 1
        return aces
        
    def get_value(self):
        pass


if __name__ == "__main__":
    pass