# PyBingoGenerator

This is a python script to create bingo cards.

The scrip creates individual bingo cards from a .txt-file with individual fieldnames and saves them as a .jpg-file.

## How to use

You have to run the script from the commandline with parameters.

The following arguments are available

- `--num_players` or `-p`: Numbers of cards to generate. Default value 1.
- `--num_fields` or `-f`: Number of total fields. Has to be a square number. Default value 25.
- `--prompts_path` or `-fp`: Path to the .txt-file with the prompts (fieldnames). This parameter has to be set. Every prompt in the .txt-file has to be a new line. The number of prompts has to be the minimum number of fields.
- `--out_path` or `-o`: Path to directory where the cards will be saved. Optional. 

Example: `python bingo_generator.py --num_players 4 --num_fields 16 --prompts_path ./test.txt`

## Example of Bingocard
(old)
For a fun evening of Eurovision.

![Bingo_nr3](https://user-images.githubusercontent.com/43641879/168441731-c5ce0174-fc73-49a3-9e19-70b7557e0a1a.jpg)

## Contributer
[Ivo Opitz](https://github.com/dont-ask-why)
