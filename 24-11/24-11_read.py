import csv

class Building:
    def __init__(self, floors, height, width, name):
        self.floors = floors
        self.height = height
        self.width = width
        self.name = name

    @classmethod
    def from_tuple(cls, data):
        return cls(*data)

buildings: list = [Building for _ in range(100)]

with open('buildings', 'rt') as file:
    csv_reader = csv.reader(file)
    buildings_csv = [Building.from_tuple(building) for building in csv_reader]
    for i in range(len(buildings_csv)):
        print('Здание', i + 1, ':', 'Количество этажей:', buildings_csv[i].floors, 'Высота:', buildings_csv[i].height,
        'Ширина:', buildings_csv[i].width, 'Название:', buildings_csv[i].name)
