import unittest
from DataReader import DataReader
from Positioner import Positioner

class TestPositioner(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.positioner = Positioner(data_reader)
        return super().setUp()

    def test_getPositionsDict(self):
        self.assertEqual(self.positioner.positions_dict, {0: 1, 1: 2, 2: 3, 3: 0, 4: 1, 5: 0, 6: 0, 7: 1, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 1, 15: 0, 16: 1})

    def test_getFactorList(self):
        self.assertEqual(self.positioner.factor_list, {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45, 10: 55, 11: 66, 12: 78, 13: 91, 14: 105, 15: 120, 16: 136})

    def test_getSpentFuelFor2(self):
        self.assertEqual(self.positioner.get_spent_fuel()[2], 37)

    def test_getSpentFuelFor1(self):
        self.assertEqual(self.positioner.get_spent_fuel()[1], 41)

    def test_getSpentFuelFor3(self):
        self.assertEqual(self.positioner.get_spent_fuel()[3], 39)

    def test_getSpentFuelFor10(self):
        self.assertEqual(self.positioner.get_spent_fuel()[10], 71)

    def test_partOne(self):
        self.assertEqual(self.positioner.part_one(), 37)

    def test_getSpentFuelExpensiveFor5(self):
        self.assertEqual(self.positioner.get_spent_fuel_expensive()[5], 168)

    def test_getSpentFuelExpensiveFor2(self):
        self.assertEqual(self.positioner.get_spent_fuel_expensive()[2], 206)

    def test_getSpentFuelExpensiveFor4(self):
        self.assertEqual(self.positioner.get_spent_fuel_expensive()[4], 170)

    def test_getSpentFuelExpensiveFor14(self):
        self.assertEqual(self.positioner.get_spent_fuel_expensive()[14], 607)

    def test_partTwo(self):
        self.assertEqual(self.positioner.part_two(), 168)

if __name__ == '__main__':
    unittest.main()
