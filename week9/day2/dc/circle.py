import math

class Circle:

    # TODO: You should implement __lt__, __le__, __eq__, __ne__, __ge__ 
    
    @staticmethod
    def sort_circles(*args):
        return sorted(args, key=lambda b: b.radius)

    def __init__(self,radius=None,diameter=None):
        self.__validate_inputs(radius,diameter)
        self.radius = radius if radius else diameter//2

    def calculate_area(self):
        return round(math.pi * self.radius**2,)

    def __add__(self,other):
        return Circle(self.radius + other.radius)
    
    def __gt__(self,other):
        return self.radius > other.radius

    def __eq__(self,other):
        return self.radius == other.radius

    def __validate_inputs(self,radius,diameter):
        # if radius == None and diameter == None:  
        if not radius and not diameter:
            raise Exception("You must pass a radius or a Diameter")
        if radius and diameter and not radius*2 == diameter:
            raise Exception(f"The radius {radius} needs to be half the diameter {diameter}")
    


# c1 = Circle()
# c2 = Circle(10,15)

c3 = Circle(10,20)
c4 = Circle(20,40)
c6 = Circle(20,40)
c5 = c3 + c4
if c3 > c4:
    print("c3 is bigger")
else:
    print("c4 is bigger")

if c6 == c4:
    print("Both circles are equal")

print(Circle.sort_circles(c3,c4,c5,c6))
 

print(c5.radius)
print(c3.calculate_area())