# Write a Python program that creates two threads to find and print even and odd numbers
# from 30 to 50.

import threading

# class EvenAndOddClass(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         self.odd_nums()
#         self.even_nums()

def odd_nums():
    for num in range(31,50,2):
        print(num, '------odd-------')   
def even_nums():
    for num in range(30,50,2):
        print(num, '-------even-------')

odd = threading.Thread(target=odd_nums)
even = threading.Thread(target=even_nums)

odd.start()
even.start()

# odd.join()
# even.join()