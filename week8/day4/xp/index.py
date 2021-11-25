#ex1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Tiger(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class MyCats()

#ex2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self, sound):
        self.sound = sound
        print(f'{self.name}{self.sound}')
    
    def run_speed(self, run_speed):
        self.run_speed = run_speed
        return f'{self.weight} / {self.age} * 10'

    def fight(self, fight):
        self.fight = fight
        
        
        
        