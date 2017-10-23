from cards import CardDeck
from scene import *


class CardScene(Scene):
    
    def setup(self):
        self.background_color = '#006300'
        self.deck = CardDeck()
        self.hand = []
        self.create_sprites()
        self.deck.shuffle()
        self.show_deck()
        self.show_hand()
        
    def touch_began(self, touch):
        if touch.location in self.deck.sprite.frame:
            self.hand += self.deck.deal(7)
            self.show_hand()
        
        for card in self.hand:
            if touch.location in card.sprite.frame:
                self.deck.add_to_top(card)
                self.hand.remove(card)
                card.sprite.remove_from_parent()
    
    def create_sprites(self):
        self.deck.sprite = SpriteNode('card:BackBlue4', scale=0.4)
        for card in self.deck.deck:
            card.sprite = SpriteNode('card:{}{}'.format(card.suit, card.rank), scale=0.4)
  
    def show_deck(self):
        pos = (50, self.size.h - 100)

        self.deck.sprite.position = pos
        self.add_child(self.deck.sprite)
        
    def card_setup(self):
        gap = self.size.w / 8
        x = gap
            
  
    def show_hand(self):
        gap = self.size.w / (len(self.hand) + 1)
        x = gap
        for card in self.hand:
            card.sprite.position = (x, 50)
            self.add_child(card.sprite)
            x += gap


run(CardScene())
