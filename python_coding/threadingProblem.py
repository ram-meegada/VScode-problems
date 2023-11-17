# Write a Python program that creates two threads to find and print even and odd numbers
# from 30 to 50.

import threading

class Snosdf():
    def funct(self):
        EvenAndOddClass(1).start()  


class EvenAndOddClass(threading.Thread):
    def __init__(self, count):
        self.count = count
        threading.Thread.__init__(self)
    def run(self):
        self.count += 1
        print(self.count, '-----------------')
        return None

a = Snosdf()
print(a.funct())





# def odd_nums():
#     for num in range(31,50,2):
#         print(num, '------odd-------')   
# def even_nums():
#     for num in range(30,50,2):
#         print(num, '-------even-------')

# odd = threading.Thread(target=odd_nums)
# even = threading.Thread(target=even_nums)

# odd.start()
# even.start()

# odd.join()
# even.join()