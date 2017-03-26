import unittest
import level


class LevelTestCase(unittest.TestCase):

    def test_generate(self):
        default_level = level.generate()

        self.assertEqual(len(default_level), 8)
        self.assertEqual(len(default_level[0]), 8)

        resized_level = level.generate(10, 5)

        self.assertEqual(len(resized_level), 5)
        self.assertEqual(len(resized_level[0]), 10)

        flat_level = sum(level.generate(), [])

        self.assertIn('T', flat_level)

    def test_run_path(self):
        level1 = [
            ['.', '.', '.'],
            ['.', 'T', '.'],
            ['.', 'T', '.'],
        ]
        level2 = [
            ['.', 'T', '.', '.'],
            ['.', '.', 'T', '.']
        ]

        self.assertEqual(level.run_path(level1, ['R', 'D', 'D']), (2, 3))
        self.assertEqual(level.run_path(level1, [], (1, 1)), (1, 0))
        self.assertEqual(level.run_path(level2, ['R', 'U']), (1, 2))
        self.assertEqual(level.run_path(level2, ['L', 'U', 'L'], (3, 1)), (2, 3))


if __name__ == '__main__':
    unittest.main()
