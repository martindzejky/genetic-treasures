import random
from copy import deepcopy
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
    level = deepcopy(original_level)

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
            if tile in tile_to_color.keys():
                colored_tile = colored(tile, tile_to_color[tile])
            else:
                colored_tile = tile

            if start[0] == x and start[1] == y:
                if tile == '.':
                    print(colored('S', tile_to_color['S']), '', end='')
                elif tile == 'T':
                    print(colored('T', tile_to_color['S']), '', end='')
                else:
                    print(colored_tile, '', end='')
            else:
                print(colored_tile, '', end='')

        print()

    # print legend
    for tile in tile_to_color:
        if tile in tile_to_desc.keys():
            print(colored(tile, tile_to_color[tile]), '=', tile_to_desc[tile], '', end='')
    print()


def print_level_path(original_level, path, start=(0, 0)):
    """ Print a level with the taken path through it. """

    # mappings
    char_to_dir = {
        'U': (0, -1),
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0)
    }
    char_to_print = {
        'U': '^',
        'R': '>',
        'D': 'v',
        'L': '<'
    }

    # make copies
    pos = tuple(start)
    level = deepcopy(original_level)

    for direction in path:
        # mark the path to the level
        tile = original_level[pos[1]][pos[0]]
        if pos[0] == start[0] and pos[1] == start[1]:
            level[pos[1]][pos[0]] = colored(char_to_print[direction], 'green')
        elif tile == 'T':
            level[pos[1]][pos[0]] = colored(char_to_print[direction], 'yellow')
        else:
            level[pos[1]][pos[0]] = char_to_print[direction]

        # move according to the direction
        pos = (pos[0] + char_to_dir[direction][0], pos[1] + char_to_dir[direction][1])

        # if out of level, stop
        if pos[0] < 0 or pos[0] >= len(level[0]):
            break
        if pos[1] < 0 or pos[1] >= len(level):
            break

    # print the level
    print_level(level, start)
