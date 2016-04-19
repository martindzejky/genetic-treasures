from functools import reduce
import random
import machine


def generate(size=64):
    """Generate a random gene"""

    return [random.randrange(255) for x in range(size)]


def generate_pool(size=64):
    """Generate a pool of genes"""

    return [generate() for x in range(size)]


def process_pool(pool, level):
    """Calculate fitness for each gene in the pool"""

    return list(map(
        lambda x: (x, machine.run(machine.interpret(x), level)), pool))


def select_parent(pool, fitness_sum):
    """Select 1 parent"""

    fitness_acc = 0
    parent = random.randrange(fitness_sum)
    for gene_fitness in pool:
        fitness_acc += gene_fitness[1]
        if fitness_acc >= parent:
            return gene_fitness[0]


def cross_parents(pool, fitness_sum, mutation_chance=2):
    """Select 2 parents according to their fitness"""

    parent1 = select_parent(pool, fitness_sum)
    parent2 = select_parent(pool, fitness_sum)

    child1 = list(parent1)
    child2 = list(parent2)
    for i in range(random.randrange(len(child1))):
        child1[i], child2[i] = child2[i], child1[i]

    # TODO: mutate just bits
    for i in range(len(child1)):
        if random.randrange(100) < mutation_chance:
            child1[i] = random.randrange(255)
    for i in range(len(child2)):
        if random.randrange(100) < mutation_chance:
            child2[i] = random.randrange(255)

    return child1, child2


def generate_new_pool(pool):
    """Make a new pool from the old one"""

    fitness_sum = reduce(lambda x, y: x + y, map(lambda x: x[1], pool))
    result = []
    for i in range(round(len(pool) / 2)):
        child1, child2 = cross_parents(pool, fitness_sum)
        result.append(child1)
        result.append(child2)

    return result
