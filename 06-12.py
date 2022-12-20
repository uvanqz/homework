from multiprocessing import Process, Queue, Event, Lock
from random import randint
from time import sleep

class Client:
    def __init__(self, name):
        self.name = name

class Barber:
    TIMEOUT = 20
    WORK_INTERVAL = (6, 8)

    def __init__(self, database: dict):
        self.database = database
        self.__client_came = Event()

    def sleep(self):
        print('В приёмной клиентов нет. Парикмахер спит')
        sleep_result = self.__client_came.wait(timeout=Barber.TIMEOUT)
        return sleep_result, self.database

    def call(self):
        self.__client_came.set()
    
    def cut(self, client: Client):
        sleep(randint(*Barber.WORK_INTERVAL))
        print('Парикмахер стрижёт клиента {}'.format(client.name))

    def greet(self, client: Client):
        print('Парикмахер пришёл в приёмную и поприветствовал клиента {}'.format(client.name))
        self.__client_came.clear()
        self.cut(client)
        print('Клиент {} пострижен'.format(client.name))
        print('Клиент {} ушёл из салона'.format(client.name))


class Salon:
    def __init__(self, database: dict, q_size: int, mutex: Lock):
        self.database = database
        self.q_size = q_size
        self.mutex = mutex
        self.__queue = Queue(maxsize=q_size)
        self.__worker = Barber(database)
        self.__process = Process(target=self.work)

    def open(self):
        print('Салон открылся')
        self.__process.start()

    def close(self):
        print('Парикмахер проснулся. Клиентов давно нет. Салон закрылся')

    def work(self):
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                self.mutex.release()
                sleep_result, database = self.__worker.sleep()
                self.database = database
                if not sleep_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.greet(client)

    def enter(self, client: Client):
        with mutex:
            print('Клиент {} пришёл в салон'.format(client.name))
            if self.__queue.full():
                print('Клиент {} увидел полную очередь и ушёл из салона'. format(client.name))
            else:
                values = client.name
                print('Клиент {} хочет модную стрижку. Ожидает в приёмной'.format(*values))
                self.__queue.put(client)
                self.__worker.call()
            
SIZE_QUEUE = 2
CLIENT_ENTER_INTERVAL = (3, 4)

if __name__ == '__main__':
    mutex = Lock()
    database = {}

    clients: list = [Client(str(i)) for i in range(1, 10)]
    salon = Salon(database, SIZE_QUEUE, mutex)
    salon.open() 
    for client in clients:
        sleep(randint(*CLIENT_ENTER_INTERVAL))
        salon.enter(client)
