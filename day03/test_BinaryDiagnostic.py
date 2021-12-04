import unittest
import os
from BinaryDiagnostic import BinaryDiagnostic

class TestBinaryDiagnostic(unittest.TestCase):

    def setUp(self) -> None:
        self.file = open('data_test', 'w')
        self.file.write("00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010")
        self.file.close()
        self.file = open('data_test', 'r')
        self.binary_diagnostic = BinaryDiagnostic(self.file.read())
        self.processed_data = [7, 5, 8, 7, 5]
        return super().setUp()

    def tearDown(self):
        self.file.close()
        os.remove('data_test')
        return super().tearDown()

    def test_processData(self):
        self.assertEqual(self.binary_diagnostic.process_data(), self.processed_data)

    def test_getGamma(self):
        self.assertEqual(self.binary_diagnostic.get_gamma(self.processed_data), 22)

    def test_getEpsilon(self):
        self.assertEqual(self.binary_diagnostic.get_epsilon(22), 9)

    def test_partOne(self):
        self.assertEqual(self.binary_diagnostic.part_one(), 198)

    def test_getBitsCounter(self):
        self.assertEqual(self.binary_diagnostic.get_bits_counter(self.binary_diagnostic.data, 0), [('1', 7), ('0', 5)])

    def test_getOxygenGeneratorRating(self):
        self.assertEqual(self.binary_diagnostic.get_oxygen_generator_rating(), 23)

    def test_getCo2ScrubberRating(self):
        self.assertEqual(self.binary_diagnostic.get_co2_scrubber_rating(), 10)

    def test_partTwo(self):
        self.assertEqual(self.binary_diagnostic.part_two(), 230)

if __name__ == '__main__':
    unittest.main()
