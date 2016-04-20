import random
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


def select_parent(population, fitness_sum):
    """Select a parent using the roulette."""

    roulette = random.randrange(fitness_sum)
    fitness_acc = 0

    for pair in population:
        fitness_acc += pair[0]
        if fitness_acc > roulette:
            return pair[1]


def evolve(population, fitness_sum):
    """Evolve the next generation from the current."""

    sorted_pop = sorted(population, key=lambda x: x[0], reverse=True)
    best_part = sorted_pop[:round(len(sorted_pop) / 2)]
    evolved = []

    for i in best_part:
        parent1 = select_parent(best_part, fitness_sum)
        parent2 = select_parent(best_part, fitness_sum)

        child1, child2 = inset.crossover(parent1, parent2)

        evolved.append(child1)
        evolved.append(child2)

    while len(evolved) < len(population):
        evolved.append(inset.generate())

    return evolved
