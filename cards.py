import random


class Card:
    '''A single playing card'''
    
    def __init__(self, suit, rank, value):
        self._suit = suit
        self._rank = rank
        self._value = value
    
    def __str__(self):
        return '{} of {}'.format(self._rank, self._suit)
        
    def __repr__(self):
        return 'Card({}, {})'.format(self._suit, self._rank)
        


class CardDeck: 
    '''A standard 52-card deck of playing cards'''
    
    def __init__(self):
        self.deck = []
        self.trash = []
        self.removed = []
        
        for s in ("Diamonds", "Hearts", "Spades", "Clubs"):
            self.deck.append(Card(s, "A", 1))
            for r in range(2, 11):
                self.deck.append(Card(s, r, r))
            for v, r in enumerate(("J", "Q", "K"), 11):
                self.deck.append(Card(s, r, v))
    
    def __str__(self):
        return 'Card Deck / Draw pile: {} / Discard pile {}'\
        .format(str(len(self.deck)),\
        str(len(self.trash)))
        
    def __repr__(self):
        return 'CardDeck()'
        
    def show_deck(self):
        '''
        Prints all cards currently in the deck.
        '''
        for card in self.deck:
            print(card)
            
    def shuffle(self, qty=1):
        '''
        Randomly shuffles the deck a specified number of times. Defaults to 1.
        '''
        amt = len(self.deck) - 1
        for count in range(qty):
            for i in range(amt, 0, -1):
                rng = random.randint(0, i)
                card = self.deck[i]
                self.deck[i] = self.deck[rng]
                self.deck[rng] = card
            
    def deal(self, qty=1):
        '''
        Removes and returns a list containing a specified number of cards from the deck. Defaults to 1.
        '''
        card_list = []
        for count in range(qty):
            card = self.deck.pop()
            self.removed.append(card)
            card_list.append(card)
        return card_list
    
    def burn(self, qty=1):
        '''
        Puts cards from the top of the deck into the discard pile. Defaults to 1.
        '''
        for count in range(qty):
            self.trash.append(self.deck.pop())
    
    def discard(self, cards):
        '''
        Input: List or Tuple
        Receives a list of cards to put into the discsrd pile
        '''
        for card in cards:
            self.trash.append(card)
    
    def shuffle_into(self, cards):
        '''
        Adds a single Card or list of Card objects into the deck and shuffles.
        '''
        pass

    def add_to_top(self, cards):
        '''
        Adds a single card or list/tuple of card objects on top of the deck in order, resulting in the last card of the list or tuple on top.
        '''
        if isinstance(cards, Card):
            self.deck.append(cards)
            if cards in self.removed:
                self.removed.remove(cards)
            
        elif isinstance(cards, list) or isinstance(cards, tuple):
            for card in cards:
                self.deck.append(card)
                if card in self.removed:
                    self.removed.remove(card)
