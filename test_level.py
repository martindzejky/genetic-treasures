import unittest
import level


class TestLevel(unittest.TestCase):

    def test_generate(self):
        world = level.generate(2, 4)

        self.assertIsInstance(world, tuple)
        self.assertIsInstance(world[0], tuple)
        self.assertEqual(len(world), 4)
        self.assertEqual(len(world[0]), 2)


if __name__ == "__main__":
    unittest.main()
