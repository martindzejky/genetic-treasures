import unittest
import inset


class TestInset(unittest.TestCase):

    def test_generate(self):
        self.assertIsInstance(inset.generate(), tuple)
        self.assertEqual(len(inset.generate(10)), 10)

    def test_crossover(self):
        parent1, parent2 = (0, 1, 2, 3), (9, 8, 7, 6)
        child1, child2 = inset.crossover(parent1, parent2)

        self.assertIsInstance(child1, tuple)
        self.assertIsInstance(child2, tuple)

        for byte in child1:
            self.assertTrue(byte in parent1 or byte in parent2)
        for byte in child2:
            self.assertTrue(byte in parent1 or byte in parent2)


if __name__ == "__main__":
    unittest.main()
