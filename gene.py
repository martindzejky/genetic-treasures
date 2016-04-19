from functools import reduce
import random
import machine


def generate(size=64):
    """Generate a random gene"""

    random_part = random.randrange(size / 4)
    for i in range(size):
        if i < random_part:
            yield random.randrange(256)
        else:
            yield 0


def generate_pool(size=64):
    """Generate a pool of genes"""

    return (list(generate()) for x in range(size))


def process_pool(pool, level):
    """Calculate fitness for each gene in the pool"""

    return map(lambda x: (x, machine.run(machine.interpret(x), level)), pool)


def select_parent(pool, fitness_sum):
    """Select 1 parent"""

    fitness_acc = 0
    parent = random.randrange(fitness_sum)
    for gene_fitness in pool:
        fitness_acc += gene_fitness[1]
        if fitness_acc >= parent:
            return gene_fitness[0]


def cross_parents(pool, fitness_sum, mutation_chance=5):
    """Select 2 parents according to their fitness"""

    parent1 = list(select_parent(pool, fitness_sum))
    parent2 = list(select_parent(pool, fitness_sum))

    # TODO: mutate just bits
    child1 = list(parent1)
    child2 = list(parent2)
    for i in range(random.randrange(len(child1))):
        child1[i], child2[i] = child2[i], child1[i]

    return child1, child2


def generate_new_pool(pool):
    """Make a new pool from the old one"""

    pool_list = list(pool)
    fitness_sum = reduce(lambda x, y: x + y, map(lambda x: x[1], pool_list))
    for i in range(round(len(pool_list) / 2)):
        child1, child2 = cross_parents(pool_list, fitness_sum)
        yield child1
        yield child2
