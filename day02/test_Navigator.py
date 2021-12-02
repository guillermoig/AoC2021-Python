import unittest
import os
from Navigator import Navigator

class TestNavigator(unittest.TestCase):

    def setUp(self) -> None:
        self.navigator = Navigator()
        self.file = open('data_test', 'w')
        self.file.write("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2")
        self.file.close()
        self.file = open('data_test', 'r')
        return super().setUp()

    def tearDown(self):
        self.file.close()
        os.remove('data_test')
        return super().setUp()

    def test_setCourseInstructions(self):
        self.navigator.set_course_instructions(self.file.read())
        self.assertEqual(self.navigator.get_set_instructions(), {'forward': [5, 8, 2], 'down': [5, 8], 'up': [3]})

    def test_positionCalculator(self):
        self.navigator.set_course_instructions(self.file.read())
        self.assertEqual(self.navigator.position_calculator(), {'horizontal': 15, 'depth': 10})

    def test_getPositionMultiplication(self):
        self.navigator.set_course_instructions(self.file.read())
        self.assertEqual(self.navigator.get_position_multiplication(), 150)

if __name__ == '__main__':
    unittest.main()
