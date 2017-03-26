import unittest
import population


class PopulationTestCase(unittest.TestCase):

    def test_generate(self):
        self.assertEqual(len(population.generate()), 100)

        for inset_size in [10, 100]:
            for pop_size in [20, 200]:
                pop = population.generate(pop_size, inset_size)

                self.assertEqual(len(pop), pop_size)
                for inset in pop:
                    self.assertEqual(len(inset), inset_size)

    def test_score(self):
        pop = [[(3 << 6) + 1, 140], [(3 << 6) + 1, 100]]
        level = [
            ['.', '.'],
            ['T', '.']
        ]

        self.assertEqual(
            population.score(pop, level, (0, 0), 1),
            [999, 0]
        )
        self.assertEqual(
            population.score(pop, level, (0, 1), 1),
            [999, 999]
        )

    def test_select_parent(self):
        self.assertEqual(population.select_parent(['a', 'b'], [100, 0]), 'a')
        self.assertEqual(population.select_parent(['a', 'b'], [0, 10]), 'b')

        pop = ['a', 'b', 'c', 'd', 'e', 'f']
        scores = [1, 1, 1, 1, 1, 1]
        for _ in range(10):
            self.assertIn(population.select_parent(pop, scores), pop)

    def test_evolve(self):
        level = [
            ['.', '.', '.'],
            ['T', 'T', 'T']
        ]

        original_population = population.generate()
        original_scores = population.score(original_population, level)
        new_population = population.evolve(original_population, original_scores)

        self.assertEqual(len(original_population), len(new_population))

        for new_inset in new_population:
            self.assertEqual(len(new_inset), len(original_population[0]))


if __name__ == '__main__':
    unittest.main()
