import unittest
import os
from DepthMeasurer import DepthMeasurer

class TestDepthMeasurer(unittest.TestCase):

    def setUp(self) -> None:
        self.depth_measurer = DepthMeasurer()
        self.file = open('data_test', 'w')
        self.file.write("199\n200\n208\n210\n200\n207\n240\n269\n260\n263")
        self.file.close()
        self.file = open('data_test', 'r')
        return super().setUp()

    def tearDown(self):
        self.file.close()
        os.remove('data_test')
        return super().setUp()

    def test_setMeasures(self):
        self.depth_measurer.set_measures("1\n23\n45")
        self.assertEqual(self.depth_measurer.get_measures(), [1, 23, 45])

    def test_increasesCounter1(self):
        self.depth_measurer.set_measures("1\n23\n45\n18\n22")
        self.assertEqual(self.depth_measurer.increases_counter(), 3)

    def test_increasesCounter2(self):
        self.depth_measurer.set_measures(self.file.read())
        self.assertEqual(self.depth_measurer.increases_counter(), 7)

if __name__ == '__main__':
    unittest.main()
