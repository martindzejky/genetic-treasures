import unittest
import level
from unittest.mock import patch, call
from termcolor import colored


class LevelTestCase(unittest.TestCase):

    def test_generate(self):
        default_level = level.generate()

        self.assertEqual(len(default_level), 8)
        for row in default_level:
            self.assertEqual(len(row), 8)

        resized_level = level.generate(10, 5)

        self.assertEqual(len(resized_level), 5)
        for row in resized_level:
            self.assertEqual(len(row), 10)

        flat_level = sum(level.generate(treasure_chance=50), [])

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

    @patch('builtins.print')
    def test_print_level(self, mock_print):
        level1 = [
            ['.', '.', 'T'],
            ['.', 'T', '.']
        ]

        level.print_level(level1, (1, 0))
        mock_print.assert_has_calls([
            call(colored('.', 'grey'), '', end=''),
            call(colored('S', 'green'), '', end=''),
            call(colored('T', 'yellow'), '', end=''),
            call(),
            call(colored('.', 'grey'), '', end=''),
            call(colored('T', 'yellow'), '', end=''),
            call(colored('.', 'grey'), '', end=''),
            call()
        ])


if __name__ == '__main__':
    unittest.main()
