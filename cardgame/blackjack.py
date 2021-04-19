import random

class Card():
    
    def __init__(self, suit, rank):

        self.suit = suit
        if self.suit == "H" or self.suit == "D":
            self.colour = "red"
        else:
            self.colour = "black"

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
        random.shuffle(self.cards)


class Hand():
    pass


if __name__ == "__main__":
    pass