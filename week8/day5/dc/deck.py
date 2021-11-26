class  Card():
    def _init_(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print(f'{self.suit}{self.value}')
card = Card('spades', 7)
card.show()

