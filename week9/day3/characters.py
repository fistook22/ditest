class Character:
    
    def __init__(self, name, life = 20, attack = 10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        other.life -= 5
        print(f"{other.name} has been attacked by {self.name} and has {other.life} remaining")


class Druid(Character):

    def meditate(self):
        self.life += 10 
        self.attack -= 2
        print(f"meditating increased {self.name} life to {self.life} but his attack decreased to {self.attack}")

    def animal_help(self):
        self.attack += 5
        print(f"animal help increased {self.name} attack to {self.attack}")

    def fight(self, other):
        other.life -= (0.75 * self.life + 0.75 * self.life)
        print(f"{self.name} hurt his enemy, he now have less life then before, he has {other.life} left")
        

class Warior(Character):
    
    def brawl(self, other):
        other.life -= self.attack * 2
        self.life += self.attack * 0.5
        print(f"{self.name} damaged {other.name} life, {other.name} now has {other.life}  life left, and {self.name} got some of {other.name} life and now have {self.life} left")

    def train(self):
        self.life += 2
        self.attack += 2
        print(f"practice makes perfect, {self.name}, training got you {self.life} life and {self.attack} attack")

    def roar(self, other):
        other.attack -= 3
        print(f"{self.name} scared {other.name} so much that he lost attack, he now has {other.attack} attack left")
        
        
class Mage(Character):
    
    def curse(self, other):
        other.attack -= 2
        print(f"{self.name}s curse made {other.name} lose attack points, {other.name} now has {other.attack} attack points left")

    def summon(self):
        self.attack += 3
        print(f"{self.name} now have more attack points as you summond that demon, {self.attack} attack points")

    def cast_spell(self, other):
        decrease = self.attack/self.life
        other.life -= decrease
        print(f"{self.name}s spell made your enemy lose {decrease} life points")
        
        
# a = Character("fuck", 25, 25)
# c = Character("you", 20, 30)
# a.basic_attack(c)
# print(c)
       
druid = Druid("druid", 100, 50)
warior = Warior("warior", 100, 50)
mage = Mage("magician", 100, 50)

druid.meditate()
druid.animal_help()
druid.fight(warior)

warior.brawl(druid)
warior.train()
warior.roar(mage)

mage.curse(druid)
mage.summon()
mage.cast_spell(warior)

