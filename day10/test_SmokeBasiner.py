import unittest
from DataReader import DataReader
from SmokeBasiner import SmokeBasiner

class TestSmokeBasiner(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.smokeBasiner = SmokeBasiner(data_reader)
        return super().setUp()

    def test_partOne(self):
        self.assertEqual(self.smokeBasiner.part_one(), 0)

    def test_partTwo(self):
        self.assertEqual(self.smokeBasiner.part_two(), 0)

if __name__ == '__main__':
    unittest.main()
