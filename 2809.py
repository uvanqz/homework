from datetime import datetime, timedelta

#datetime — объекты даты и времени
#timedelta — этот атрибут покрывает интервалы и используется для определения прошлых или будущих событий
def capitan(tekst, data):
    next_day = timedelta(days=1)
    with open ("capitan.txt", 'w') as file:
        for element in tekst:
            file.write(str(data) + ' : ' + element + '\n')  #str преобразует данные в строку
            data = data + next_day
        file.close()
capitan(['Вышли в открытое море','Сильный ураган','Погода улучшилась', 'Виднеется земля'], datetime (2022, 10, 12))
