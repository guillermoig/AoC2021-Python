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

    def test_increasesCounter(self):
        self.depth_measurer.set_measures("1\n23\n45\n18\n22")
        self.assertEqual(self.depth_measurer.increases_counter(), 3)

    def test_increasesCounterTest(self):
        self.depth_measurer.set_measures(self.file.read())
        self.assertEqual(self.depth_measurer.increases_counter(), 7)

    def test_groupByWindow(self):
        self.depth_measurer.set_measures("1\n23\n45\n18\n22")
        self.assertEqual(self.depth_measurer.group_by_window(2), [24, 68, 63, 40])

    def test_groupByWindowTest(self):
        self.depth_measurer.set_measures(self.file.read())
        self.assertEqual(self.depth_measurer.group_by_window(3), [607, 618, 618, 617, 647, 716, 769, 792])

    def test_increasesInWindowsOfThree(self):
        self.depth_measurer.set_measures("1\n23\n45\n18\n22")
        self.assertEqual(self.depth_measurer.increases_in_windows_of_three(), 1)

    def test_increasesInWindowsOfThreeTest(self):
        self.depth_measurer.set_measures(self.file.read())
        self.assertEqual(self.depth_measurer.increases_in_windows_of_three(), 5)

if __name__ == '__main__':
    unittest.main()
