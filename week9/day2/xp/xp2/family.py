class Family:
    def __init__(self, name, age, gender, is_child = False):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_child = is_child
    
class Members(Family):
    def __init__(self, name, age, gender, is_child=False):
        super().__init__(name, age, gender, is_child=is_child)
    members = [
        {'name':'micheal', 'age':35, 'gender':'male', 'is_child':False},
        {'name':'sarah', 'age':32, 'gender':'female', 'is_child':False}
    ]
    