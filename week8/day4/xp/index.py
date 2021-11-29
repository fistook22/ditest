#ex1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat(Pets):
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return print(f'{self.name} is just walking around')

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Tiger(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# cat1 = Bengal('benny', 8)
# cat2 = Chartreux('cha', 6)
# cat3 = Tiger('tig', 5)
# my_cats = [cat1, cat2, cat3]
# my_pets = Pets(cat3)
# cat1.walk()
# cat2.walk()
# cat3.walk()

#ex2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking!')
    
    def run_speed(self):
        return self.weight / self.age * 10

        
    def fight(self,other_dog):
        if (self.weight*self.run_speed()) > (other_dog.weight *other_dog.run_speed()):
            print(f"{self.name} is the champion and he beet {other_dog.name}")
        else:
            print(f"{other_dog.name} is the champion and he beet {self.name}")

dog1 = Dog('dani', 8, 21)
dog2 = Dog('dogo', 6, 26)
dog3 = Dog('fogo', 4, 27)
dog1.run_speed()
dog1.fight(dog2)
        

     
        
        