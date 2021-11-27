import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def show(self):
        print(f'{self.value} of {self.suit}')

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ['spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10,'j','q','k']:
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i] 

    def drawCard(self):
        return self.cards.pop()
        

deck = Deck()
deck.show()
print('!!!!!!!!!!!!')
deck.shuffle()
deck.show()
card = deck.drawCard()
print('this is the card drawn')
card.show()

    




# import random

# SUITS = ['C', 'S', 'H', 'D']
# RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.build()

#     def build(self):
#         for value in RANKS:
#             for suit in SUITS:
#                 self.cards.append((value, suit))
  
#     def shuffle(self):
#         random.shuffle(self.cards)
        

#     def deal(self):
#         if len(self.cards) > 1:
#             return self.cards.pop()

