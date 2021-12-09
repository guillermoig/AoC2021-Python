import unittest
from DataReader import DataReader
from SegmentSearcher import SegmentSearcher

class TestSegmentSearcher(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.segmentSearcher = SegmentSearcher(data_reader)
        self.input = ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']
        self.input_split = [list(x) for x in self.input]
        self.known_numbers = {1: ['b','e'], 4: ['b','c','e','g'], 7: ['b','d','e'], 8: ['a','b','c','d','e','f','g']}
        self.known_numbers_with_9 = {1: ['b','e'], 4: ['b','c','e','g'], 7: ['b','d','e'], 8: ['a','b','c','d','e','f','g'], 9: ['b','c','d','e','f','g']}
        self.number_in_segments = {
            'abdefg': '0',
            'be': '1',
            'abcdf': '2',
            'bcdef': '3',
            'bceg': '4',
            'cdefg': '5',
            'acdefg': '6',
            'bde': '7',
            'abcdefg': '8',
            'bcdefg': '9'
        }
        # self.number_in_segments = {
        #     0: ['d', 'g', 'b', 'a', 'e', 'f'],
        #     1: ['b', 'e'],
        #     2: ['d', 'b', 'c', 'a', 'f'],
        #     3: ['d', 'b', 'c', 'e', 'f'],
        #     4: ['g', 'b', 'c', 'e'],
        #     5: ['d', 'g', 'c', 'e', 'f'],
        #     6: ['d', 'g', 'c', 'a', 'e', 'f'],
        #     7: ['d', 'b', 'e'],
        #     8: ['d', 'g', 'b', 'c', 'a', 'e', 'f'],
        #     9: ['d', 'g', 'b', 'c', 'e', 'f']
        # }
        return super().setUp()

    def test_partOne(self):
        self.assertEqual(self.segmentSearcher.part_one(), 26)

    def test_getKnownNumbers(self):
        self.assertEqual(self.segmentSearcher.get_known_numbers(self.input), self.known_numbers)

    def test_getSegment0(self):
        self.assertEqual(self.segmentSearcher.get_segment_0(self.known_numbers), 'd')

    def test_getSegment6(self):
        self.assertEqual(self.segmentSearcher.get_segment_6(self.known_numbers, {0: 'd'}, self.input), 'f')

    def test_getSegment4(self):
        self.assertEqual(self.segmentSearcher.get_segment_4(self.known_numbers_with_9), 'a')

    def test_getSegment2(self):
        self.assertEqual(self.segmentSearcher.get_segment_2(self.known_numbers, self.input_split), 'b')

    def test_getSegment5(self):
        self.assertEqual(self.segmentSearcher.get_segment_5(self.known_numbers, 'b'), 'e')

    def test_getSegment3(self):
        self.assertEqual(self.segmentSearcher.get_segment_3({0: 'd', 2: 'b', 4: 'a', 6: 'f'}, self.input_split), 'c')

    def test_getSegment1(self):
        self.assertEqual(self.segmentSearcher.get_segment_1({0: 'd', 2: 'b', 3: 'c', 4: 'a', 5: 'e', 6: 'f'}, self.known_numbers[8]), 'g')

    # def test_getNumbersInSegments(self):
    #     self.assertEqual(self.segmentSearcher.get_numbers_in_segments({0: 'd', 1: 'g', 2: 'b', 3: 'c', 4: 'a', 5: 'e', 6: 'f'}), self.number_in_segments)

    def test_getNumbersInSegments(self):
        self.assertEqual(self.segmentSearcher.get_numbers_in_segments({0: 'd', 1: 'g', 2: 'b', 3: 'c', 4: 'a', 5: 'e', 6: 'f'}), self.number_in_segments)

    def test_decodeOutput(self):
        self.assertEqual(self.segmentSearcher.decode_output(self.number_in_segments, ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']), 8394)

    def test_decodeOutputNumbers(self):
        self.assertEqual(self.segmentSearcher.decode_output_numbers(), {0: 8394, 1: 9781, 2: 1197, 3: 9361, 4: 4873, 5: 8418, 6: 4548, 7: 1625, 8: 8717, 9: 4315})

    def test_partTwo(self):
        self.assertEqual(self.segmentSearcher.part_two(), 61229)

if __name__ == '__main__':
    unittest.main()
