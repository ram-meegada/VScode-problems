import threading
from time import sleep

class One(threading.Thread):
    def run(self):
        for i in range(500):
            print(i, 'oneeeee')
            sleep(1)

class Two(threading.Thread):
    def run(self):
        for i in range(500):
            print(i, 'twooooo')
            sleep(1)

one = One()                        
two = Two()
one.start()                        
two.start()                        