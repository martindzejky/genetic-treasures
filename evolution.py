import population


def run(level, generations=500):
    """Run the evolution for a number of generations."""

    population = population.generate()
    print("initial population size is", len(population.insets))

    for i in range(generations):
        print("\b" * 256, end="")
        print("generation", i, end="")
