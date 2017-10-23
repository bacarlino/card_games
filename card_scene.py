from cards import CardDeck
from scene import *


class CardScene(Scene):
    
    def setup(self):
        self.background_color = '#006300'
        self.deck = CardDeck()
        self.create_sprites()
        
    def create_sprites(self):
        self.deck.sprite = SpriteNode('card:BackBlue4', scale=0.4)
        for card in self.deck.deck:
            card.sprite = SpriteNode('card:{}{}'.format(card.suit, card.rank), scale=0.4)
 
 
if __name__ == '__main__':
    run(CardScene())
