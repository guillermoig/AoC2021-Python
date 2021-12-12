import unittest
from DataReader import DataReader
from DumboOctopus import DumboOctopus

class TestDumboOctopus(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test1")
        self.dumbo_octopus = DumboOctopus(data_reader)
        return super().setUp()

    def test_runStep1Time(self):
        map = "34543\n40004\n50005\n40004\n34543"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep2Times(self):
        map = "45654\n51115\n61116\n51115\n45654"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_getFlashesAfter1Time(self):
        self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.get_flashes(), 9)

    # def test_partOne(self):
    #     self.assertEqual(self.dumbo_octopus.part_one(), 0)

    # def test_partTwo(self):
    #     self.assertEqual(self.dumbo_octopus.part_two(), 0)

if __name__ == '__main__':
    unittest.main()
