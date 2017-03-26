from argparse import ArgumentParser
from typing import List
from termcolor import colored
import sys
import level
import population
import machine
import instruction_set


def fitness_color(fitness: float, number_of_treasures: int) -> str:
    """ Generate a proper color for a fitness for printing. """

    color = 'red'
    if fitness > 1000:
        color = 'yellow'
    if fitness > number_of_treasures / 3 * 2000:
        color = 'green'

    return colored(fitness, color)


def percent_color(percentage: float) -> str:
    """ Generate a proper color for a percentage for printing. """

    color = 'red'
    if percentage > 30:
        color = 'yellow'
    if percentage > 70:
        color = 'green'

    return colored(percentage, color)


def format_path(path: List[str]) -> str:
    """ Nicely format a path. """

    lookup = {
        'U': '^',
        'R': '>',
        'D': '<',
        'L': 'v'
    }

    return ''.join(map(lambda d: lookup[d], path))


def main():
    """ The main entry point. Runs the evolution and displays
        the progress and the results. """

    help_string = 'A great adventure to find all treasures! Use the genetic algorithm to evolve' \
                  ' the best possible instruction set. A virtual machine interprets the instructions' \
                  ' and generates a path. A greedy guy in the generated level follows the path and' \
                  ' collects the treasures in the level.'
    url_string = 'https://github.com/chuckeles/genetic-treasures'

    # first, set up and parse command line options
    parser = ArgumentParser(description=help_string, epilog=url_string)

    parser.add_argument('-lw', '--width', type=int, default=8, help='level width (default: %(default)s)')
    parser.add_argument('-lh', '--height', type=int, default=8, help='level height (default: %(default)s)')
    parser.add_argument('-tc', '--treasure-chance', type=int, default=10,
                        help='chance that a treasure will be generated, in percents (default: %(default)s)')
    parser.add_argument('-s', '--start', type=int, default=[0, 0], nargs=2,
                        help='starting position of the guy collecting treasures (default: %(default)s)')
    parser.add_argument('-p', '--population', type=int, default=100, help='population size (default: %(default)s)')
    parser.add_argument('-is', '--instruction-size', type=int, default=64,
                        help='size of the instruction set (default: %(default)s)')
    parser.add_argument('-n', '--number-of-generations', type=int, default=200,
                        help='number of generations to run the evolution for (default: %(default)s)')
    parser.add_argument('-pp', '--print-progress', type=int, default=10,
                        help='print progress every N generations (default: %(default)s)')
    parser.add_argument('-mi', '--machine-iterations', type=int, default=500,
                        help='maximum number of iterations the virtual machine can make (default: %(default)s)')
    parser.add_argument('-mc', '--mutation-chance', type=int, default=5,
                        help='mutation chance for new instruction sets (default: %(default)s)')
    parser.add_argument('-cr', '--crossover-random', action='store_true',
                        help='if specified, the crossover takes each byte randomly from either parent,'
                             ' instead of taking continuous parts from both parents (default: %(default)s)')
    parser.add_argument('-mf', '--mutation-function', choices=['bit', 'byte'], default='bit',
                        help='mutation function to use - either mutate just bits or the whole bytes'
                             ' (choices: %(choices)s) (default: %(default)s)')

    args = parser.parse_args()

    # generate a level
    print('Generating a level of size', colored('%d×%d' % (args.width, args.height), 'blue'), 'with treasure chance',
          colored(args.treasure_chance, 'yellow'))

    generated_level = level.generate(args.width, args.height, args.treasure_chance)
    level.print_level(generated_level, args.start)

    # count the number of treasures
    number_of_treasures = sum(generated_level, []).count('T')
    print('There are', colored(number_of_treasures, 'yellow'), 'treasures in total')
    print()

    # generate a population
    print('Generating the initial population of', colored(args.population, 'blue'), 'instruction sets with size',
          colored(args.instruction_size, 'blue'))
    print()
    current_population = population.generate(args.population, args.instruction_size)

    generation = 0

    # repeat until all treasures are found or the user stops
    while True:

        # run the evolution
        try:
            print('Running the evolution for', colored(args.number_of_generations, 'blue'), 'generations')
            for iteration in range(args.number_of_generations):
                m_f = instruction_set.mutate_bits if args.mutation_function == 'bits' else instruction_set.mutate_bytes

                # score the current population and evolve a new one
                current_scores = population.score(current_population, generated_level, start=args.start,
                                                  max_machine_iterations=args.machine_iterations)
                current_population = population.evolve(current_population, current_scores,
                                                       mutation_chance=args.mutation_chance,
                                                       crossover_take_random=args.crossover_random,
                                                       mutation_function=m_f)

                # increase generation number
                generation += 1

                # print progress
                if iteration % args.print_progress == 0:
                    avg_fitness = sum(current_scores) / len(current_scores)
                    print('\b' * 256, end='')
                    print('Generation number', colored(generation, 'blue'), 'has average fitness',
                          fitness_color(avg_fitness, number_of_treasures), 'and the best fitness is',
                          fitness_color(max(current_scores), number_of_treasures), end='')
                    print(' ' * 16, end='')
                    sys.stdout.flush()

            print()
            print(colored('Finished', 'green'), 'the evolution')

        # allow the user to stop the evolution
        except KeyboardInterrupt:
            print()
            print(colored('Stopping', 'red'), 'the evolution')

        print()

        # score the final population
        final_population = current_population
        final_scores = population.score(final_population, generated_level, start=args.start,
                                        max_machine_iterations=args.machine_iterations)

        # find the best path
        best_inset = final_population[0]
        best_score = final_scores[0]
        for i, inset in enumerate(final_population):
            if final_scores[i] > best_score:
                best_score = final_scores[i]
                best_inset = inset

        best_path = machine.interpret(best_inset, max_iterations=args.machine_iterations)
        collected_treasures, steps_taken = level.run_path(generated_level, best_path, start=args.start)
        collected_percent = round(collected_treasures / number_of_treasures * 100, 2)

        # print the path, the fitness, and the treasures taken
        print('The best instruction set has fitness', fitness_color(best_score, number_of_treasures))
        print('The generated path is:', colored(format_path(best_path[:steps_taken]), 'cyan'))
        print('The guy collected', colored(collected_treasures, 'yellow'), 'treasures',
              '(' + percent_color(collected_percent) + '%)')

        # check if all treasures are collected
        if collected_treasures == number_of_treasures:
            break
        else:
            # offer to continue or stop evolving
            try:
                print()
                answer = input('The best path does not yet collect all treasures, do you want to keep running?'
                               ' [' + colored('y', 'green') + '/' + colored('N', 'red') + '] ')
                print()

                if answer != 'y' and answer != 'Y':
                    break

            # interrupt can also be used as a no
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()
