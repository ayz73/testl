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
