import unittest
import population


class TestPopulation(unittest.TestCase):

    def test_generate(self):
        self.assertIsInstance(population.generate(), tuple)
        self.assertEqual(len(population.generate(10)), 10)


if __name__ == "__main__":
    unittest.main()
