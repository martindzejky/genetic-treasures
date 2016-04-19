import random


def generate(size: int):
    """Generate a new level"""

    return tuple(
        tuple(1 if random.randrange(100) < 20 else 0 for x in range(size))
        for x in range(size))


def print_level(level: tuple):
    """Print a level"""

    for row in level:
        for place in list(map(lambda x: "P " if x == 1 else "O ", row)):
            print(place, end="")
        print()
