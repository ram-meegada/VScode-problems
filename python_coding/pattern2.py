# Create a function generate_pattern that takes a character and a number as parameters.
# The function should print a pattern where the character is repeated in each row, and the 
# number determines the number of rows. Use default parameters for 
# character ('*') and number (5).

def generate_pattern(character, number):
    for i in range(1, number+1):
        for j in range(i):
            print(character, end = " ")
        print()    

char = "*"
num = 5
generate_pattern(char, num)