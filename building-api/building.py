class Crud:
    def create(self, type):
        _entity = self.__class__(type)
        self.items.append(_entity)

    def read(self, idx):
        return self.items[idx]

    def update(self, idx, value):
        if len(self.items) == 0:
            self.items.append(value)
        else:    
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

building.create('floor')
print('floors', building.items)

floor2 = building.read(2)
print('rooms', floor2.items)
floor2.update(0, room1)
floor2.update(0, room1)
print('rooms', floor2.items)
print(floor2.items)

building.remove(1)

print(building.items)



