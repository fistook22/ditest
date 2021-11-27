import index
import random

class PetDog(index.Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark()) and self.trained = True

    def play(self, *args):
        print(f'{args} all play together')

    def do_a_trick(self):
        self.trick_list = [f'{self} does a barrel roll', f'{self} stands on his back legs', f'{self} shakes your hand', f'{self} playes dead']
        # self.roll = f'{self} does a barrel roll'
        # self.stand = f'{self} stands on his back legs'
        # self.shake = f'{self} shakes your hand'
        # self.dead = f'{self} playes dead'
        if self.trained is True:
            print(random(self.trick_list))
                    
                
        
    
