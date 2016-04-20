import unittest
import machine


class TestMachine(unittest.TestCase):

    def test_interpret_inset(self):
        inset = (0, 1, 70, 80, 140, 180, 200)
        path = machine.interpret_inset(inset)

        self.assertIsInstance(path, tuple)
        self.assertEqual(path[0], (-1, 0))
        self.assertEqual(path[1], (-1, 0))
        self.assertEqual(path[2], (0, -1))
        self.assertEqual(path[3], (0, -1))
        self.assertEqual(path[4], (1, 0))
        self.assertEqual(path[5], (1, 0))
        self.assertEqual(path[6], (0, 1))

    def test_run_path(self):
        level = ((0, 0), (0, 1))
        start = (0, 0)
        path1 = ((1, 0), (-1, 0))
        path2 = ((1, 0), (0, 1))

        self.assertEqual(machine.run_path(level, (), start), 1)
        self.assertEqual(machine.run_path(level, path1, start), 1)
        self.assertEqual(machine.run_path(level, path2, start), 999)


if __name__ == "__main__":
    unittest.main()
