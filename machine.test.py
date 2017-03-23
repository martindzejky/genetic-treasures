import unittest
import machine


class MachineTestCase(unittest.TestCase):

    def test_interpret(self):
        # increment 0, print 0, jump to 0, increment 1, print 1, jump to 0, increment 1, print 2
        inset = [0, 3 << 6, 2 << 6]

        print_up = [(3 << 6) + 1, 0]
        print_right = [(3 << 6) + 1, 100]
        print_down = [(3 << 6) + 1, 140]
        print_left = [(3 << 6) + 1, 200]

        self.assertIsInstance(machine.interpret(inset), list)

        self.assertEqual(machine.interpret(print_up, max_iterations=1), ['U'])
        self.assertEqual(machine.interpret(print_right, max_iterations=1), ['R'])
        self.assertEqual(machine.interpret(print_down, max_iterations=1), ['D'])
        self.assertEqual(machine.interpret(print_left, max_iterations=1), ['L'])

        self.assertEqual(machine.interpret(inset, max_iterations=8), ['U', 'L', 'D'])


if __name__ == '__main__':
    unittest.main()
