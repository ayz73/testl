from blackjack import Card, Deck
import unittest

class card_test(unittest.TestCase):
    def test_card_init(self):
        self.assertEqual(str(Card("H", 11)), "HJ")
        self.assertEqual(str(Card("S", 1)), "SA")
        self.assertEqual(str(Card("D", 10)), "D10")

class deck_test(unittest.TestCase):
    def test_deck_init(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertTrue(Card("S", 13) in deck.cards)
        self.assertTrue(Card("D", 1) in deck.cards)

if __name__ == "__main__":
    unittest.main()