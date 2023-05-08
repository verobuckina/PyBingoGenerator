import textwrap as twp
import argparse
import random
import math
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--num_players', type=int, default=1)
parser.add_argument('-f', '--num_fields', type=int, default=25)
parser.add_argument('-fp', '--prompts_path', type=str)
parser.add_argument('-o', '--out_path', type=str, default='.')
args = parser.parse_args()

def main():
    if not args.prompts_path:
        print('You have to give the path for the .txt-file for the prompts.')
        return

    num_players = args.num_players # input from user on number of unique bingo cards to generate
    num_fields = args.num_fields # Input from user on side length of square bingo matrix
    list = [] # list of all possible bingo field fillers
    path = args.prompts_path

    print('------ Bingo Generator ------')
    try: 
        with open(path, encoding='utf8') as f:
            list = f.readlines()
            f.close()

        size = int(math.sqrt(num_fields))
        if int(size + 0.5) ** 2 != num_fields:
            print('Number of fields has to be square.')
            return
 
        # check if list has enough entrys
        len_list = len(list)
        if len_list < num_fields:
            print('Prompt list to short.')
            return

        for user in range(num_players):
            img_size = (512, 512)
            image = Image.new(mode='L', size=img_size, color=255)

            cell_size = int(512 / size)
            fontsize = 10

            draw = ImageDraw.Draw(image)
            for i in range(0, 512, cell_size):
                line = ((i, 0), (i, 512))
                draw.line(line, fill=128)
                line = ((0, i), (512, i))
                draw.line(line, fill=128)
            
            rand_prompts = random.sample(list, num_fields)
            i = 0
            for x in range(size):
                for y in range(size):
                    prompt = rand_prompts[i]
                    para = twp.fill(prompt, width=int(cell_size/fontsize))
                    w, h = draw.textsize(para)
                    draw.text(((cell_size - w)/2 + x * cell_size, (cell_size - h)/2 + y * cell_size),
                                para, 
                                fill=0)
                    i += 1

            card_path = f'{args.out_path}/Bingo_nr{user}.jpg'
            image.save(card_path)
            print(f'Bingo card saved as: {card_path}')

    except KeyboardInterrupt:
        print("\nExiting...")
        exit()

if __name__ == '__main__':
    main()