import inset
import machine


def generate(size=100):
    """Generate a population of random insets."""

    return tuple(inset.generate() for i in range(size))


def score(population, level, start):
    """Assign fitness to every inset in the population."""

    return tuple(map(lambda inset: (machine.run_path(
                                    level,
                                    machine.interpret_inset(inset),
                                    start),
                                    inset),
                     population
                     ))
