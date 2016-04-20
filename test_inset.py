import unittest
import inset


class TestInset(unittest.TestCase):

    def test_generate(self):
        self.assertIsInstance(inset.generate(), tuple)
        self.assertEqual(len(inset.generate(10)), 10)


if __name__ == "__main__":
    unittest.main()
