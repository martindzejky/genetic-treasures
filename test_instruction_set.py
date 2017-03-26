import unittest
import instruction_set


class TestInstructionSet(unittest.TestCase):

    def test_generate(self):
        self.assertIsInstance(instruction_set.generate(), list)

        self.assertEqual(len(instruction_set.generate()), 64)
        self.assertEqual(len(instruction_set.generate(32)), 32)

        inset = instruction_set.generate()
        for instruction in inset:
            self.assertGreaterEqual(instruction, 0)
            self.assertLess(instruction, 256)

    def test_crossover(self):
        parent1 = instruction_set.generate()
        parent2 = instruction_set.generate()

        children = instruction_set.crossover(parent1, parent2)
        random_children = instruction_set.crossover(parent1, parent2, take_random=True)

        self.assertIsInstance(children, tuple)
        self.assertIsInstance(children[0], list)
        self.assertIsInstance(children[1], list)

        self.assertEqual(len(children[0]), len(parent1))
        self.assertEqual(len(children[1]), len(parent1))

        for i, _ in enumerate(parent1):
            self.assertTrue(
                (children[0][i] in parent1 and children[1][i] in parent2) or
                (children[0][i] in parent2 and children[1][i] in parent1)
            )
            self.assertTrue(
                (random_children[0][i] in parent1 and random_children[1][i] in parent2) or
                (random_children[0][i] in parent2 and random_children[1][i] in parent1)
            )

    def test_mutate_bits(self):
        inset = instruction_set.generate()

        self.assertEqual(len(inset), len(instruction_set.mutate_bits(inset)))
        self.assertEqual(inset, instruction_set.mutate_bits(inset, mutation_chance=0))
        self.assertNotEqual(inset, instruction_set.mutate_bits(inset, mutation_chance=100))

        for instruction in instruction_set.mutate_bits(inset):
            self.assertGreaterEqual(instruction, 0)
            self.assertLess(instruction, 256)

    def test_mutate_bytes(self):
        inset = instruction_set.generate()

        self.assertEqual(len(inset), len(instruction_set.mutate_bytes(inset)))
        self.assertEqual(inset, instruction_set.mutate_bytes(inset, mutation_chance=0))
        self.assertNotEqual(inset, instruction_set.mutate_bytes(inset, mutation_chance=100))

        for instruction in instruction_set.mutate_bytes(inset):
            self.assertGreaterEqual(instruction, 0)
            self.assertLess(instruction, 256)

    def test_mutate_combined(self):
        inset = instruction_set.generate()

        self.assertEqual(len(inset), len(instruction_set.mutate_combined(inset)))

        for instruction in instruction_set.mutate_combined(inset):
            self.assertGreaterEqual(instruction, 0)
            self.assertLess(instruction, 256)


if __name__ == '__main__':
    unittest.main()
