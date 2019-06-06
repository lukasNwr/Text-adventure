from creatures.creature import Creature
from creatures.creatureType import CreatureType

class Ork(Creature):
    
    def __init__(self):
        super().__init__(100, 10, CreatureType.ENEMY)
        self.name = "ork"
    
    def printHealth(self):
        print(self.health)