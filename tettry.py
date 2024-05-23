import random as r

# valid_words =[]
# with open ('C:\\Users\\ucbra\\OneDrive\\Desktop\\Documents\\Desktop\\UC Academy\\Anaya\\Python Intermidiate\\Collins Scrabble Words (2019).txt') as f:
#     for line in f:
#         temp = line.strip('\n')
#         valid_words.append(temp)
    
# print(valid_words)
# def int_input(prompt):
#     num = input(prompt)
#     while num.isdigit() == False:
#         print("you did it wrong >:( try again")
#         num = input(prompt)
#     num = int(num)
#     return num

# a = int_input('Enter a number: ')
# print(a,type(a))

# def str_input(prompt):
#     word = input(prompt)
#     while word.isalpha() == False:
#         print("omg stop getting it wrong")
#         word = input(prompt)
#     return word.upper()

# b = str_input('enter a wordie:')
# print(b)
TILES = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A',
         'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'R', 'T', 'N',
         'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'L', 'S', 'U', 'L', 'S', 'U', 'L',
         'S', 'U', 'L', 'S', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'C', 'M', 'P', 'B', 'C', 'M', 'P',
         'F', 'H', 'V', 'W', 'Y', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']

# tile_to_points maps a letter to the number of points it is worth when played
tile_to_points = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                  'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
                  'Q': 10, 'Z': 10}

def get_new_tiles(num):
    hand = r.sample(get_new_tiles,num)
    num.remove(hand)
    '''
    The parameter 'num' is how many tiles the user needs.
    It should fetch 'num' RANDOM tiles from the TILES list.
    Then, remove each of these tiles from the TILES list.
    Return this list of random tiles.

    HINT: What do we need at the TOP of the code in order to use randomness?
    '''
    pass