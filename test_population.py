import unittest
import population
import level
import evolution


class TestPopulation(unittest.TestCase):

    def test_generate(self):
        self.assertIsInstance(population.generate(), tuple)
        self.assertEqual(len(population.generate(10)), 10)

    def test_score(self):
        pop = population.generate()

        for pair in population.score(pop, level.generate(), (0, 0)):
            self.assertGreaterEqual(pair[0], 1)
            self.assertIsInstance(pair[1], tuple)

    def test_evolve(self):
        pop = population.generate()
        scored_pop = population.score(pop, level.generate(), (0, 0))
        fitness_sum = evolution.count_fitness_sum(scored_pop)
        evolved_pop = population.evolve(scored_pop, fitness_sum)

        self.assertEqual(len(pop), len(evolved_pop))


if __name__ == "__main__":
    unittest.main()
