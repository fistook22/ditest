class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, animal_amount = 1):
        if animal_type in self.animals:
            self.animals[animal_type] = self.animals[animal_type] +animal_amount
        else:
            self.animals[animal_type] = animal_amount
            
        self.animals[animal_type] = animal_amount


    def get_info(self):
        print(f"{self.farm_name}'s farm\n")

        for animal_type, animal_amount in self.animals.items():
            print(f'{animal_type}: {animal_amount}')
        return '\n\tE-I-E-I-O!'

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())