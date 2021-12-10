import unittest
from DataReader import DataReader
from SyntaxScoring import SyntaxScoring

class TestSyntaxScoring(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.syntaxScoring = SyntaxScoring(data_reader)
        return super().setUp()

    def test_partOne(self):
        self.assertEqual(self.syntaxScoring.part_one(), 0)

    def test_partTwo(self):
        self.assertEqual(self.syntaxScoring.part_two(), 0)

if __name__ == '__main__':
    unittest.main()
