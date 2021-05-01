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
    def test_aces(self):
        cards_list = [Card("S", 1), Card("H", 11), Card("D", 1)]
        hand = Hand(cards_list)
        self.assertEqual(hand.aces(), 2)
        cards_list.append(Card("C", 1))
        self.assertEqual(hand.aces(), 2)

        hand_2 = Hand([])
        self.assertEqual(hand_2.aces(), 0)
    
    def test_hand_value(self):
        hand = Hand([Card("S", 3), Card("D", 12)])
        self.assertEqual(hand.hand_value(), {13})

        cards_list = [Card("S", 1), Card("H", 7), Card("D", 1)]
        hand_2 = Hand(cards_list)
        self.assertEqual(hand_2.hand_value(), {9, 19})

        hand_3 = Hand([Card("D", 1), Card("C", 1)])
        self.assertEqual(hand_3.hand_value(), {2, 12})


if __name__ == "__main__":
    unittest.main()