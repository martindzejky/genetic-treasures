import random
import machine


def generate(size: int = 64):
    """Generate a random gene"""

    return bytes([random.getrandbits(8) for x in range(size)])


def generate_pool(size: int = 64):
    """Generate a pool of genes"""

    return tuple(generate() for x in range(50))


def process_pool(pool: tuple, level: tuple):
    """Calculate fitness for each gene in the pool"""

    return tuple(map(
        lambda x: (x, machine.run(machine.interpret(x), level)), pool))
