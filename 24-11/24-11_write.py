import csv

class NotValidBuilding(Exception):
    pass

class Building:
    def __init__(self, floors, height, width, name):
        self.floors = floors
        self.height = height
        self.width = width
        self.name = name
        if not self.is_valid():
            raise NotValidBuilding
            
    def is_valid(self):
        properties = [self.floors, self.height, self.width]
        if all([isinstance(element, (int, float)) for element in properties]):
            return all([element > 0 for element in properties])

    def to_tuple(self):
        return self.floors, self.height, self.width, self.name

building_1 = Building(1, 2, 3, 'aaa')
building_2 = Building(3, 4, 5, 'bbb')
building_3 = Building(5, 6, 7, 'ccc')
building_4 = Building(7, 8, 9, 'ddd')
building_5 = Building(9, 10, 11, 'eee')


buildings: list = [building_1, building_2, building_3, building_4, building_5]

with open('buildings', 'wt') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows([building.to_tuple() for building in buildings])
