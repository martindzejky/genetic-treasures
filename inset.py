import random


def generate(size=64):
    """Make a new inset."""

    return tuple(random.randrange(255) for i in range(size))
