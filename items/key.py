from items.item import Item

class Key(Item):

    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)