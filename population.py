import random
import instruction_set
import machine
import level


def generate(size=100, instruction_set_size=64):
    """ Generate a new population of instruction sets. """

    return [instruction_set.generate(instruction_set_size) for _ in range(size)]


def score(population, generated_level, start=(0, 0), max_machine_iterations=500):
    """ Score the entire population. """

    def score_instruction_set(inset):
        path = machine.interpret(inset, max_machine_iterations)
        found_treasures, steps_taken = level.run_path(generated_level, path, start)

        return max(0, found_treasures * 1000 - steps_taken)

    return [score_instruction_set(inset) for inset in population]


def select_parent(population, scores):
    """ Select a parent using the roulette. """

    fitness_acc = 0
    fitness_sum = sum(scores)

    # if fitness sum is 0, just select a random parent
    if fitness_sum == 0:
        return random.choice(population)

    roulette = random.randrange(fitness_sum)

    for i, inset in enumerate(population):
        fitness_acc += scores[i]
        if fitness_acc > roulette:
            return inset

    return population[0]


def evolve(population, scores, mutation_function=instruction_set.mutate_bits, mutation_chance=5, crossover_take_random=False):
    """ Evolve the next population from the current one. """

    # join the population with the scores
    scored_population = map(lambda inset, inset_score: (inset, inset_score), population, scores)

    # sort the population based on the scores
    sorted_population = sorted(scored_population, key=lambda i: i[1])

    # take the best half (correction: third)
    half_point = round(len(sorted_population) / 3 * 2)
    best_half = sorted_population[half_point:]

    # split again to population and score
    best_half_population = list(map(lambda i: i[0], best_half))
    best_half_scores = list(map(lambda i: i[1], best_half))

    new_generation = []

    # produce offspring of the best parents in the population
    for _ in best_half:
        parent1 = select_parent(best_half_population, best_half_scores)
        parent2 = select_parent(best_half_population, best_half_scores)

        child1, child2 = instruction_set.crossover(parent1, parent2, crossover_take_random)

        # mutate the children and insert to the new pool
        new_generation.append(mutation_function(child1, mutation_chance))
        new_generation.append(mutation_function(child2, mutation_chance))

    # add random instruction sets and return the new population
    random_to_add = len(population) - len(new_generation)
    return new_generation + [instruction_set.generate(len(new_generation[0])) for _ in range(random_to_add)]
