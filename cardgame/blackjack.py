import random
import sys

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
        
        if not self.face:
            self.value = rank
        elif self.face != "A":
            self.value = 10
        else:
            self.value = 0
        
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

    def shuffle(self):
        random.shuffle(self.cards)
    
    def hand_out(self, hand, amount):
        for _ in range(amount):
            card = self.cards.pop()
            hand.add_card(card)


class Hand():
    
    def __init__(self, cards=None):
        self.cards = []
        self.cards += cards

    def add_card(self, card):
        self.cards.append(card)
    
    def aces(self):
        aces = 0
        for card in self.cards:
            if card.face == "A":
                aces += 1
        return aces
        
    def hand_value(self):
        hand_value = 0
        for card in self.cards:
            hand_value += card.value

        all_values = []

        ace_amount = self.aces()
        if ace_amount == 0:
            return set([hand_value])
        else:
            for i in range(ace_amount):
                all_values.append(hand_value + ace_amount + i * 10)
        
        ed_all_values = [i for i in all_values if i <= 21]
        return set(ed_all_values)


def num_check(text):
    while True:
        try:
            num = int(input(text))
            if num > 0:
                return num
            else:
                print("Please input a positive number...")
        except ValueError:
            print("Please input a valid number...")
            continue


if __name__ == "__main__":
    player_count = num_check("How many players would be playing?")

    while True:
        deck = Deck()
        
        dealer = Hand()
        deck.hand_out(dealer, 2)
        if dealer.hand_value() == 21:
            continue

        players = {}
        for i in range(player_count):
            players["player_%s" % (i)] = Hand()

