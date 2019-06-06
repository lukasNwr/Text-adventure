from creatures.creature import Creature

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.creaturesInRoom = []

    def setDescription(self, decription):
        self.description = description

    def getDescription(self):
        if len(self.creaturesInRoom) != 0:
            self.description += "\nCreatures in room: "
            for creature in self.creaturesInRoom:
                self.description += creature.name + ", "
            return self.description
        else:
            return self.description 

    def addCreature(self, creature):
        if isinstance(creature, Creature):
            self.creaturesInRoom.append(creature)
    
    def getCreaturesInRoom(self):
        return self.creaturesInRoom