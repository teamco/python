class Crud:
    def create(self, type):
        _entity = self.__class__(type, self)  # Entity(type)
        self.items.append(_entity)
        self.removeItems = []

    def read(self, idx):
        return self.items[idx]

    def update(self, idx, value):
        if len(self.items) == 0:
            self.items.append(value)
        else:
            self.items[idx] = value

    def remove(self, idx):
        print('Remove', self.type, 'item', self.index, idx)
        items = self.items[idx].items
        while(len(items) > 0):
            items[0].parent.remove(0)

        return self.items.pop(idx)

    def print_all(self):
        for i, element in enumerate(self.items):
            if (len(element.items) > 0):
                print(element.type, i)
                element.print_all()
            else:
                print(element.type, i)

class Entity(Crud):
   # Hierarchy = ["Building", "floor", "room", "table"]

    def __init__(self, type, parent):
        self.type = type
        self.parent = parent
        self.index = 0
        if (parent != None):
            self.index = len(parent.items)
        self.items = []


building = Entity('Building', None)

#print(building)
#print(building.type)

building.create('floor-1')
building.create('floor-2')
building.create('floor-3')

floor1 = building.read(0)
floor1.create('room-1.1')
#floor1.create('room')

floor2 = building.read(1)
floor2.create('room-2.1')
floor2.create('room-2.2')

floor3 = building.read(2)
floor3.create('room-3.1')

room1 = floor2.read(0)
room1.create('table-2.1.1')
room1.create('trash-2.1.2')

building.print_all()
print("************")
floor2.remove(0)
print("************")
building.print_all()

# building.create('floor')
# print('floors', building.items)

# floor2 = building.read(2)
# print('rooms', floor2.items)
# floor2.update(0, room1)
# floor2.update(0, room1)
# print('rooms', floor2.items)
# print(floor2.items)

# building.remove(1)

# print(building.items)
