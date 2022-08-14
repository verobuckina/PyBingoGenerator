import numpy as np
import matplotlib.pyplot as plt
import textwrap as twp

count = 1 # input from user on number of unique bingo cards to generate
size = 5 # Input from user on side length of square bingo matrix
list = [] # list of all possible bingo field fillers
path = './ESC-Bingo-Fields.txt'

print('------ Bingo Generator ------')
try: 
    print('Enter number of players: ')
    count = int(input())

    print('Enter size of bingo card (i.e. for 5x5 enter 5): ')
    size =int(input())

    print('Enter path to txt file with Bingo entrys:')
    path = input()

    with open(path, encoding='utf8') as f:
        list = f.readlines()
        f.close()

    list = np.array(list)

    for user in range(count):
        rng = np.random.default_rng()
        list_identifiers = rng.choice(a=list, size=(size**2), replace=False)

        # here: export the stuff to plt
        plt.figure(figsize=(15,15), facecolor='xkcd:light blue grey')
        
        for i in range(1, size**2 + 1):
            subplt = plt.subplot(size, size, i)
            plt.xticks([])
            plt.yticks([]) 
            plt.text(0.5, 0.5, twp.fill(list_identifiers[i-1], 25), horizontalalignment='center', verticalalignment='center')

        file_name = 'Bingo_nr' + str(user) + '.jpg'
        
        plt.savefig(file_name)
        
except KeyboardInterrupt:
    print("\nExiting...")
    exit()
except ValueError:
    print("Invalid input. Input has to be an integer.")
    exit()