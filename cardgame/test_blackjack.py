from blackjack import Card, Deck, Hand
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
    
class hand_test(unittest.TestCase):
    def test_get_aces(self):
        cards_list = [Card("S", 1), Card("H", 11), Card("D", 1)]
        hand = Hand(cards_list)
        self.assertEqual(hand.get_aces(), 2)
        cards_list.append(Card("C", 1))
        self.assertEqual(hand.get_aces(), 2)

        hand_2 = Hand([])
        self.assertEqual(hand_2.get_aces(), 0)
    
    


if __name__ == "__main__":
    unittest.main()