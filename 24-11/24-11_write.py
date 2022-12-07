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

buildings = list()
print('Введите количество зданий: ')
chislo_buildings = int(input())

for i in range(chislo_buildings):
    building = Building(int(input("Введите количество этажей здания {}: ".format(i+1))), int(input("Введите высоту здания {}: ".format(i+1))), int(input("Введите ширину здания {}: ".format(i+1))), input("Введите название здания {}: ".format(i+1)))
    buildings.append(building)

with open('buildings_file', 'wt') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows([building.to_tuple() for building in buildings])
