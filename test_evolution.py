import unittest
import evolution


class TestEvolution(unittest.TestCase):

    def test_count_fitness_sum(self):
        self.assertEqual(
            evolution.count_fitness_sum(
                ((1, ()), (10, ()), (5, ()))
            ), 16)
        self.assertEqual(
            evolution.count_fitness_sum(
                ((20, ()), (10, ()), (4, ()), (6, ()), (50, ()))
            ), 90)


if __name__ == "__main__":
    unittest.main()
