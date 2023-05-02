#TODO 1: Movement test on atlas map
#TODO 2: Connect world_time, current_time to age

class Entity:
    def __init__(self, age, genome="", position=(0,0), base_speed=0, hp=10):
        self.age = age
        self.genome = genome
        self.position = position
        self.base_speed = base_speed
        self.hp = hp

class Animal(Entity):
    def __init__(self, age):
        super().__init__(age, base_speed=1)
        self.state = "idle"
    
    def move(self, x, y):
        self.position = (self.position[0] + x*self.base_speed, self.position[1] + y*self.base_speed)

class Plant(Entity):
    def __init__(self, age):
        super().__init__(age, base_speed=0)
        self.state = "idle"

class Tree(Plant):
    def __init__(self, age):
        super().__init__(age)
        self.state = "growing"

class Mushroom(Plant):
    def __init__(self, age):
        super().__init__(age)
        self.state = "dying"

class Human(Animal):
    def __init__(self, age):
        super().__init__(age)
        self.state = "idle"