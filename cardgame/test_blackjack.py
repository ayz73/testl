from blackjack import Card
import unittest

class card_test(unittest.TestCase):
    def test_cards_init(self):
        self.assertEqual(str(Card("H", 11)), "HJ")
        self.assertEqual(str(Card("S", 1)), "SA")
        self.assertEqual(str(Card("D", 10)), "D10")

if __name__ == "__main__":
    unittest.main()