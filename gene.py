from functools import reduce
import random
import machine


def generate(size: int = 64):
    """Generate a random gene"""

    return bytes([random.getrandbits(8) for x in range(size)])


def generate_pool(size: int = 64):
    """Generate a pool of genes"""

    return tuple(generate() for x in range(size))


def process_pool(pool: tuple, level: tuple):
    """Calculate fitness for each gene in the pool"""

    return tuple(map(
        lambda x: (x, machine.run(machine.interpret(x), level)), pool))


def count_fitness_sum(pool: tuple):
    """Count sum of fitness"""

    return reduce(lambda x, y: x + y, map(lambda x: x[1], pool))


def select_parent(pool: tuple, fitness_sum: int):
    """Select 1 parent"""

    fitness_acc = 0
    parent = random.randrange(fitness_sum)
    for gene_fitness in pool:
        fitness_acc += gene_fitness[1]
        if fitness_acc >= parent:
            return gene_fitness[0]


def cross_parents(pool: tuple, mutation_chance: int = 15):
    """Select 2 parents according to their fitness"""

    fitness_sum = count_fitness_sum(pool)
    parent1 = select_parent(pool, fitness_sum)
    parent2 = select_parent(pool, fitness_sum)

    return bytes(
        [random.choice([parent1[i], parent2[i]]) if random.randrange(100) > mutation_chance
            else random.getrandbits(8) for i in range(len(parent1))])


def generate_new_pool(pool: tuple):
    """Make a new pool from the old one"""

    return tuple(cross_parents(pool) for x in range(len(pool)))
