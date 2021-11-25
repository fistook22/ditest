#ex1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1 = Cat('miaoo', 11)
# cat2 = Cat('mitzi', 3)
# cat3 = Cat('shoko', 5)
# oldest_cat = max(cat1.age, cat2.age, cat3.age)



# print(cat1.name, cat1.age)
# print(cat2.name, cat2.age)
# print(cat3.name, cat3.age)
# print(oldest_cat)



#ex2
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     def bark(self):
#         print(f'{self.name} goes woof!')
#     def jump(self):
#         x = self.height * 2
#         print(f'{self.name} jumps {x}cm high!')


# def height(a,b,c,d,e,f):
#     if a>b and b>c:
#         return print(d +' is taller')
#     elif c>a and b>a:
#         return print(f + ' is taller')
#     else:
#         return print(d + ' is taller')
        

# dog1 = Dog('Parker', 65)
# davids_dog = Dog('Rex', 50)
# saras_dog = Dog('Teacup', 20)

# dog1.bark()
# dog1.jump()
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()
# print(saras_dog.name, saras_dog.height)
# saras_dog.bark()
# saras_dog.jump()
# height(dog1.height, davids_dog.height, saras_dog.height, dog1.name
# , davids_dog.name
# , saras_dog.name
# )

#ex3
# class Song:
#     def __init__(self, lyrics: list):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         return print(self.lyrics)
        

# stairway = Song(["There’s a lady who's sure","all that glitters is gold",
#  "and she’s buying a stairway to heaven"])

# sing = print(stairway.sing_me_a_song())


#ex4
from operator import add


class zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name

    def animals(self, animals : list):
        self.animals = animals
    
    def add_animal(self, new_animal):
        self.new_animal = new_animal
        if new_animal not in zoo.animals:
            new_animal = self.add_animal
            
    def get_animals(self, pr_animals):
        self.pr_animals = pr_animals
        print()
                
        
        