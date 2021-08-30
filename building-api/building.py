class Crud:
    def create(self, type):
        _entity = self.__class__(type)
        self.items.append(_entity)

    def read(self, idx):
        return self.items[idx]

    def update(self, idx, value):
        self.items[idx] = value  

    def remove(self, idx):
        self.items.pop(idx)        


class Entity(Crud):
    def __init__(self, type):
        self.type = type
        self.items = []

building = Entity('Building')

print(building)
print(building.type)

building.create('floor')
building.create('floor')

floor1 = building.read(1)
floor1.create('room')

room1 = floor1.read(0)

print(floor1.type)
print(floor1.items)
print(room1.type)

print(building.items)

building.remove(1)

print(building.items)
