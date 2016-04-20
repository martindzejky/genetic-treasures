import random


def generate(size=(7, 7), treasure_change=10):
    """Generate a random level."""

    return tuple(tuple(0 if random.randrange(100) < treasure_change else 1
                       for x
                       in range(size[0]))
                 for y
                 in range(size[1])
                 )
