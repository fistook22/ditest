class City:
    def __init__(self, name, buildings = []):
        self.name = name
        self.buildings = buildings
        pass

    def construct(self, address):
        self.address = address
        self.buildings.__add__
        pass

    def info(self, address):
        pass


    class Building:
        def __init__(self, address, inhabitants = []):
            self.address = address
            self.inhabitants = inhabitants


        class Human:
            def __init__(self, name, age, living_place = None):
                self.name = name
                self.age = age
                self.living_place = living_place

            def move(self, building):
                self.living_place = building
                City.Building.inhabitants.__add__(self, self.name)

    




        
         
city = City.Building("TLV", None)     
building1 = City.Building(1, "st")
avi = City.Building.Human("avi", 30, 1)
avi.move(building1)
print(building1.inhabitants)