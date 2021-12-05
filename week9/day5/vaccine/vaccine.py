import queue
from typing import List


class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.family = None
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

    def family(self):
        self.family = []

    def add_family_member(self, person):
        if self in person:
            self.family += self.person


class Queue:

    queue = []
    person1 = ""
    person2 = ""

    def __init__(self, humans: List[Human]):
        self.humans = humans

    def add_person(self, person):
        if self.age >= 60 or person.priority == true:
            self.queue.append(person, 0)
        else:
            return queue.append(person, -1)

    def find_in_queue(self, person):
        for person in queue:
            return self.index(person)

    def swap(self, person1, person2):
        self.person2 = self.index(person1)
        self.person1 = self.index(person2)

    def get_next(self):
        return self.next

    def get_next_blood_type(self, blood_type):
        return self.person1.bloodtype

    def sort_by_age(self):
        return queue.sorted(-1, 0)

    def rearrange_queue(self):

        if self in family:
            return
        return self.queue.__index__(self.person)


avi = Human("111", "avi", 40, True, "A")
david = Human("222", "david", 50, False, "AB")
sara = Human("333", "sara", 60, True, "O")

line = Queue([avi, david])

line.add_person(sara)
line.find_in_queue(sara)
line.get_next_blood_type(david)
print(line)