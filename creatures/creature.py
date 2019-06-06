# from creatures.creatureRelation import CreatureRelation

class Creature:

    def __init__(self, health, power, creatureType):
        self.health = health
        self.power = power
        self.state = "alive"
        self.location = None
        self.creatureType = None
        self.name = "DefaultCreature"
    

    def attack(self, deffender):
        if len(self.location.getCreaturesInRoom()) == 0:
            print("You have nobody to attack!")
        else:
            if deffender.health < self.power:
                deffender.state = "dead"
            else: 
                deffender.health -= self.power

    def setRelation(self, creatureType):
        self.creatureType = creatureType