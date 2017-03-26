import random


def generate(size=64):
    """ Generate a new instruction set. """

    return [random.randrange(256) for _ in range(size)]


def crossover(parent1, parent2, take_random=False):
    """ Cross-over 2 instruction sets. If take_random is False, selects just 1 point and
        takes the first part from set1 and the second from set2. If take_random is True,
        each instruction is taken from either set randomly. """

    if take_random:
        indices = [random.choice([1, 2]) for _ in parent1]
        child1 = []
        child2 = []

        for i, index in enumerate(indices):
            child1.append(parent1[i] if index == 1 else parent2[i])
            child2.append(parent1[i] if index == 2 else parent2[i])

        return child1, child2

    else:
        point = random.randrange(len(parent1))
        return parent2[point:] + parent1[:point], parent1[point:] + parent2[:point]


def mutate_bits(inset, mutation_chance=5):
    """ Mutate the instruction set by changing 1 bit per instruction. """

    def change_bit(byte):
        bit = 1 << random.randrange(8)
        if random.choice([True, False]):
            return byte | bit
        else:
            return byte & ~bit

    return [change_bit(i) if random.randrange(100) < mutation_chance else i for i in inset]


def mutate_bytes(inset, mutation_chance=2):
    """ Mutate the instruction set by changing whole bytes. """

    return [random.randrange(256) if random.randrange(100) < mutation_chance else i for i in inset]


def mutate_combined(inset, mutation_chance=5):
    """ Apply mutation for bits and bytes simultaneously. """

    return mutate_bits(mutate_bytes(inset, round(mutation_chance / 4)), mutation_chance)
