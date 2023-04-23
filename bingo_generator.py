import numpy as np
import matplotlib.pyplot as plt
import textwrap as twp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--num_players', type=int, default=1)
parser.add_argument('-f', '--num_fileds', type=int, default=25)
parser.add_argumnet('-p', '--fields_path', type=str)
parser.add_argument('-o', '--out_path', type=str)
args = parser.parse_args()

def main():
    if not args.fields_path and not args.out_path:
        return

    count = args.num_palyers # input from user on number of unique bingo cards to generate
    size = args.num_fields # Input from user on side length of square bingo matrix
    list = [] # list of all possible bingo field fillers
    path = args.fields_path

    print('------ Bingo Generator ------')
    try: 
        with open(path, encoding='utf8') as f:
            list = f.readlines()
            f.close()

        list = np.array(list)
        try:
            if(list.size < (size)):
                raise ValueError
        except ValueError:
            print("To few entrys in file.")
            exit()

        for user in range(count):
            rng = np.random.default_rng()
            list_identifiers = rng.choice(a=list, size=(size**2), replace=False)

            # here: export the stuff to plt
            plt.figure(figsize=(15,15), facecolor='xkcd:light blue grey')
            
            for i in range(1, size + 1):
                subplt = plt.subplot(size, size, i)
                plt.xticks([])
                plt.yticks([]) 
                plt.text(0.5, 0.5, twp.fill(list_identifiers[i-1], 25), horizontalalignment='center', verticalalignment='center')

            file_name = 'Bingo_nr' + str(user) + '.jpg'
            
            plt.savefig(file_name)

    except KeyboardInterrupt:
        print("\nExiting...")
        exit()

if __name__ == '__main__':
    main()