import random
from termcolor import colored


def generate(width=8, height=8, treasure_chance=10):
    """ Generates a new random level. """

    return [[
        '.' if random.randrange(100) > treasure_chance else 'T'
        for _ in range(width)] for _ in range(height)]


def run_path(original_level, path, start=(0, 0)):
    """ Run the path in a level and return the number
        of collected treasures and the number of steps taken. """

    # dictionary with mappings between direction chars and tuples
    char_to_dir = {
        'U': (0, -1),
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0)
    }

    collected_treasures = 0
    steps_taken = 0

    # make copies
    pos = tuple(start)
    level = [list(row) for row in original_level]

    # if we start on a treasure, collect it
    if level[pos[1]][pos[0]] == 'T':
        collected_treasures += 1
        level[pos[1]][pos[0]] = '.'

    for direction in path:
        # move according to the direction
        pos = (pos[0] + char_to_dir[direction][0], pos[1] + char_to_dir[direction][1])
        steps_taken += 1

        # if out of level, stop
        if pos[0] < 0 or pos[0] >= len(level[0]):
            break
        if pos[1] < 0 or pos[1] >= len(level):
            break

        # collect treasure
        if level[pos[1]][pos[0]] == 'T':
            collected_treasures += 1
            level[pos[1]][pos[0]] = '.'

    return collected_treasures, steps_taken


def print_level(level, start=(0, 0)):
    """ Print a level to the console. """

    # lookup dictionaries
    tile_to_color = {
        '.': None,
        'T': 'yellow',
        'S': 'green'
    }
    tile_to_desc = {
        '.': 'empty tile',
        'T': 'treasure',
        'S': 'start'
    }

    # print the level
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if start[0] == x and start[1] == y:
                print(colored('S', tile_to_color['S']), '', end='')
            else:
                print(colored(tile, tile_to_color[tile]), '', end='')

        print()

    # print legend
    for tile in tile_to_color:
        print(colored(tile, tile_to_color[tile]), '=', tile_to_desc[tile], '', end='')
    print()
