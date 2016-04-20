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
        fitness_avg = fitness_sum / len(scored_pop)

        if i % 64 == 0:
            color = 31
            if fitness_avg > 3000:
                color = 32
            elif fitness_avg > 1100:
                color = 33

            print("\b" * 256, end="")
            print("generation\033[36m",
                  i,
                  "\033[0m& average fitness is\033[" + str(color) + "m",
                  fitness_avg,
                  "\033[0m",
                  end="")
            sys.stdout.flush()

        pop = population.evolve(scored_pop, fitness_sum)

    print()
    pop = population.score(pop, level, start)

    best_pair = pop[0]
    for pair in pop:
        if pair[0] > best_pair[0]:
            best_pair = pair

    return best_pair
