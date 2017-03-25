import random


def generate(width=8, height=8, treasure_chance=10):
    """ Generates a new random level. """

    return [[
        '.' if random.randrange(100) > treasure_chance else 'T'
        for _ in range(width)] for _ in range(height)]


def run_path(original_level, path, start=(0, 0)):
    """ Run the path in a level and return the number
        of collected treasures. """

    # dictionary with mappings between direction chars and tuples
    char_to_dir = {
        'U': (0, -1),
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0)
    }

    collected_treasures = 0

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

        # if out of level, stop
        if pos[0] < 0 or pos[0] >= len(level[0]):
            break
        if pos[1] < 0 or pos[1] >= len(level):
            break

        # collect treasure
        if level[pos[1]][pos[0]] == 'T':
            collected_treasures += 1
            level[pos[1]][pos[0]] = '.'

    return collected_treasures
