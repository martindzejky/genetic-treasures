import random


def generate(size=64):
    """Make a new inset."""

    return tuple(random.randrange(255) for i in range(size))


def crossover(parent1, parent2):
    """Make children by crossing parents over."""

    point = random.randrange(len(parent1))
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]


def mutate(inset, mutation_chance=5):
    """Mutate an inset."""

    return tuple(i if random.randrange(100) > mutation_chance
                 else random.randrange(255)
                 for i
                 in inset)
