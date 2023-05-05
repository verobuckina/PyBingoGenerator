import textwrap as twp
import argparse
import random
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--num_players', type=int, default=1)
parser.add_argument('-f', '--num_fields', type=int, default=5)
parser.add_argument('-fp', '--fields_path', type=str)
parser.add_argument('-o', '--out_path', type=str, default='.')
args = parser.parse_args()

def main():
    if not args.fields_path and not args.out_path:
        return

    count = args.num_players # input from user on number of unique bingo cards to generate
    size = args.num_fields # Input from user on side length of square bingo matrix
    list = [] # list of all possible bingo field fillers
    path = args.fields_path

    print('------ Bingo Generator ------')
    try: 
        with open(path, encoding='utf8') as f:
            list = f.readlines()
            f.close()

        # check if list has enough entrys
        len_list = len(list)
        if len_list < (size * size):
            print('Prompt list to short.')
            return

        for user in range(count):
            img_size = (512, 512)
            image = Image.new(mode='L', size=img_size, color=255)

            cell_size = int(512 / size)

            draw = ImageDraw.Draw(image)

            for i in range(0, 512, cell_size):
                line = ((i, 0), (i, 512))
                draw.line(line, fill=128)
                line = ((0, i), (512, i))
                draw.line(line, fill=128)
            
            rand_prompts = random.sample(list, size * size)
            i = 0

            fontsize = 10

            for x in range(size):
                for y in range(size):
                    prompt = rand_prompts[i]
                    para = twp.fill(prompt, width=int(cell_size/fontsize))
                    w, h = draw.textsize(para)
                    draw.text(((cell_size - w)/2 + x * cell_size, (cell_size - h)/2 + y * cell_size),
                                para, 
                                fill=0)
                    i += 1

            image.save(f'{args.out_path}/Bingo_nr{user}.jpg')

    except KeyboardInterrupt:
        print("\nExiting...")
        exit()

if __name__ == '__main__':
    main()