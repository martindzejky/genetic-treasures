import random


def generate(width=7, height=7, treasure_chance=10):
    """Generate a random level."""

    return tuple(tuple(0 if random.randrange(100) < treasure_chance else 1
                       for x
                       in range(width))
                 for y
                 in range(height)
                 )
