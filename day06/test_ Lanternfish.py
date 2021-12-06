import unittest
from DataReader import DataReader
from Lanternfish import Lanternfish

class TestLanternfish(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.lanternfish = Lanternfish(data_reader)
        return super().setUp()

    def test_getInitialLanternfishGroups(self):
        self.assertEqual(self.lanternfish.lanternfish_groups, [0,1,1,2,1,0,0,0,0])

    def test_getEvolutionAfter1Day(self):
        self.assertEqual(self.lanternfish.get_evolution_after_n_days(1), [1,1,2,1,0,0,0,0,0])

    def test_getEvolutionAfter10Days(self):
        self.assertEqual(self.lanternfish.get_evolution_after_n_days(10), [3,2,2,1,0,1,1,1,1])

    def test_getEvolutionAfter18Days(self):
        self.assertEqual(self.lanternfish.get_evolution_after_n_days(18), [3,5,3,2,2,1,5,1,4])

    def test_partOne(self):
        self.assertEqual(self.lanternfish.part_one(), 5934)

    def test_partTwo(self):
        self.assertEqual(self.lanternfish.part_two(), 26984457539)

if __name__ == '__main__':
    unittest.main()
