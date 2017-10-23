import unittest
from cards import *
from solitaire import *


class TestSortedPile(unittest.TestCase):
    
    def setUp(self):
        self.ace_spade = Card("Spade", "Ace" , 1)
        self.three_heart = Card("Heart", 3, 3)
        self.two_spade = Card("Spade", 2, 2)
        
        self.pile1 = SortedPile()
        self.pile2 = SortedPile()
        
    def test_add_card(self):
        self.pile1.add_card(self.ace_spade)
        self.pile1.add_card(self.three_heart)
        self.pile1.add_card(self.two_spade)
        
        self.pile2.add_card(self.three_heart)
        self.pile2.add_card(self.two_spade)
        
        self.assertIn(self.ace_spade, self.pile1.cards)
        self.assertIn(self.two_spade, self.pile1.cards)
        self.assertNotIn(self.three_heart, self.pile1.cards)
        
        self.assertNotIn(self.three_heart, self.pile2.cards)
        self.assertNotIn(self.two_spade, self.pile2.cards)
        
        
if __name__ == "__main__":
    unittest.main()
