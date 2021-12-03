import unittest
import os
from Navigator import Navigator

class TestNavigator(unittest.TestCase):

    def setUp(self) -> None:
        self.file = open('data_test', 'w')
        self.file.write("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2")
        self.file.close()
        self.file = open('data_test', 'r')
        self.navigator = Navigator(self.file.read())
        return super().setUp()

    def tearDown(self):
        self.file.close()
        os.remove('data_test')
        return super().setUp()

    def test_partOne(self):
        self.assertEqual(self.navigator.part_one(), 150)

    def test_partTwo(self):
        self.assertEqual(self.navigator.part_two(), 900)

if __name__ == '__main__':
    unittest.main()
