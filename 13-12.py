from threading import Thread, Condition, Lock
from time import sleep
from random import choice, randint, random
import string
from random import *

class Writer(Thread):

    KOLVO_BUKV = 3
    TIMEOUT = (2, 3)
    SLEEP_TIME = (3, 4)
    
    def __init__(self, name:str):
        super().__init__(name=name)

    def run(self):
        global new_text, lock, condition
        while True:
            print('Писатель {} отдохнул и хочет написать текст. Ожидает своей очереди'.format(self.name))
            lock.acquire() 
            print('Писатель {} начал писать книгу'.format(self.name))
            new_text = ''
            for kolichestvo_bukv in range(Writer.KOLVO_BUKV):
                with condition:
                    bukva = choice(string.ascii_letters)
                    new_text += bukva
                    print('Писатель {} внёс изменения в текст книги. Текст: {}'.format(self.name, new_text))
                    condition.notify_all() 
                sleep(randint(*Writer.TIMEOUT))
            print('Писатель {} дописал книгу и пошёл спать'.format(self.name))
            lock.release() 
            sleep(randint(*Writer.SLEEP_TIME))

class Reader(Thread):

    def __init__(self, name:str):
        super().__init__(name=name)

    def run(self):
        global new_text, condition
        while True:
            with condition:
                condition.wait()
                print('Читатель {} читает книгу. Текст книги: {}'.format(self.name, new_text))

WRITERS = 3
READERS = 2

if __name__ == '__main__':
    condition = Condition()
    lock = Lock() 
    new_text = ''
    for i in range(WRITERS):
        Writer(str(i)).start()
    for i in range(READERS):
        Reader(str(i)).start()
