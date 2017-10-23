import unittest
import cards


class TestCards(unittest.TestCase):
    
    
    def setUp(self):
        self.deck1 = cards.CardDeck()
        self.deck2= cards.CardDeck()
        
    def test_deck_creation(self):
        self.assertTrue(len(self.deck1.deck) == 52)
        
    def test_shuffle(self):
        pass
        
        
        
if __name__ == "__main__":
    unittest.main()
