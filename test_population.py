import unittest
import population
import level


class TestPopulation(unittest.TestCase):

    def test_generate(self):
        self.assertIsInstance(population.generate(), tuple)
        self.assertEqual(len(population.generate(10)), 10)

    def test_score(self):
        pop = population.generate()

        for pair in population.score(pop, level.generate(), (0, 0)):
            self.assertGreaterEqual(pair[0], 1)
            self.assertIsInstance(pair[1], tuple)


if __name__ == "__main__":
    unittest.main()
