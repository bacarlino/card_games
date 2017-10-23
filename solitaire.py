from card_scene import CardScene
from scene import *


class SolitaireScene(CardScene):
    
    def setup(self):
        super().setup()
        

class WorkingPile:
    def __init__(self):
        pass
    

class SortedPile:
    
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        if not self.cards and card.value == 1:
            self.cards.append(card)
        elif self.cards:
            comp_card = self.cards[-1]
            if card.suit == comp_card.suit and card.value == comp_card.value + 1:
                self.cards.append(card)
        
        
if __name__ == "__main__":
    run(SolitaireScene())


'''
deck -

game - maintains specific settings, general logic for game operation

player - can maintain games won/loss

sorted piles - initially empty. can accept new cards if consecutively higher AND same suit.

initial piles - 7 initial piles. have a specific number of both revealed and not revealed cards. Can accept a new card if consecutively higher in number AND opposite color. 
'''
