import unittest
from DataReader import DataReader
from SmokeBasiner import SmokeBasiner

class TestSmokeBasiner(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.smokeBasiner = SmokeBasiner(data_reader)
        self.map_test= [
            [2,1,9,9,9,4,3,2,1,0],
            [3,9,8,7,8,9,4,9,2,1],
            [9,8,5,6,7,8,9,8,9,2],
            [8,7,6,7,8,9,6,7,8,9],
            [9,8,9,9,9,6,5,6,7,8]
        ]
        return super().setUp()

    def test_getMap(self):
        self.assertEqual(self.smokeBasiner.map, self.map_test)

    def test_isLowPointFalse(self):
        self.assertEqual(self.smokeBasiner.is_low_point(1, 1), False)

    def test_isLowPointTrue(self):
        self.assertEqual(self.smokeBasiner.is_low_point(2, 2), True)

    def test_partOne(self):
        self.assertEqual(self.smokeBasiner.part_one(), 15)

    def test_getBasinPoints01(self):
        self.assertEqual(self.smokeBasiner.get_basin_points(0,1), {'0-1': 1, '1-1': 'X', '0-0': 2, '1-0': 3, '2-0': 'X', '0-2': 'X'})

    def test_getBasinPoints09(self):
        self.assertEqual(self.smokeBasiner.get_basin_points(0,9), {
            '0-9': 0, '1-9': 1, '2-9': 2, '3-9': 'X', '2-8': 'X', '1-8': 2, '0-8': 1, '0-7': 2,
            '1-7': 'X', '0-6': 3, '1-6': 4, '2-6': 'X', '1-5': 'X', '0-5': 4, '0-4': 'X'
        })

    def test_partTwo(self):
        self.assertEqual(self.smokeBasiner.part_two(), 1134)

if __name__ == '__main__':
    unittest.main()
