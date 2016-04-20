from functools import reduce
import sys
import population


def count_fitness_sum(scored_population):
    """Count the sum fitness of the population."""

    return reduce(lambda x, y: x + y,
                  map(lambda x: x[0], scored_population))


def run(level, start, generations=500):
    """Run the evolution for a number of generations."""

    pop = population.generate()
    print("initial population size is", len(pop))

    for i in range(generations):
        scored_pop = population.score(pop, level, start)
        fitness_sum = count_fitness_sum(scored_pop)

        if i % 16 == 0:
            print("\b" * 256, end="")
            print("generation", i, "& average fitness is",
                  fitness_sum / len(scored_pop), end="")
            sys.stdout.flush()

    print()
