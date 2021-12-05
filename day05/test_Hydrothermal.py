import unittest
from DataReader import DataReader
from Hydrothermal import Hydrothermal

class TestHydrothermal(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.hydrothermal = Hydrothermal(data_reader)
        self.line_list = [
            [0,0,0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,0,0],
            [0,1,1,2,1,1,1,2,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [2,2,2,1,1,1,0,0,0,0]
        ]
        return super().setUp()

    def test_getPairOfPoints(self):
        self.assertEqual(self.hydrothermal.pair_of_points, [[[0,0],[8,8]],[[0,2],[4,6]],[[0,7],[4,7]],[[0,8],[8,0]],[[1,2],[2,2]],[[2,8],[5,5]],[[4,1],[4,3]],[[4,3],[4,9]],[[9,0],[9,2]],[[9,0],[9,5]]])

    def test_getMaxNumberItems(self):
        self.assertEqual(self.hydrothermal.max_number_items, 10)

    def test_getLineList(self):
        self.assertEqual(self.hydrothermal.get_line_list(self.hydrothermal.pair_of_points), self.line_list)

    def test_partOne(self):
        self.assertEqual(self.hydrothermal.part_one(), 5)

    # def test_partTwo(self):
    #     self.assertEqual(self.hydrothermal.part_two(), 0)

if __name__ == '__main__':
    unittest.main()
