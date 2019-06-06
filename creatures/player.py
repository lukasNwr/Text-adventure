from room import Room
from creatures.creature import Creature
from creatures.creatureType import CreatureType

class Player(Creature):
    
    def __init__(self, name, health, location):
        super().__init__(health, 20, CreatureType.PLAYER)
        self.name = name
        self.health = health
        self.location = location

    def look(self):
        self.location.printDescription()

    