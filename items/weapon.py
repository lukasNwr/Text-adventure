from items.item import Item

class Weapon(Item):

    def __init__(self, name, description, weight, damage, speed):
        super().__init__(name, description, weight)
        self.damage = damage
        self.speed = speed