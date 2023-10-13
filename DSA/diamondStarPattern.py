spaces = 4
for i in range(1, 10, 2):
    for space in range(spaces):
        print(' ', end = '')
    spaces -= 1    
    for star in range(i):
        print('*', end='')
    print()
for i in range(9, 0, -2):
    for space in range(spaces+1):
        print(' ', end = '')
    spaces += 1    
    for star in range(i):
        print('*', end='')
    print()    