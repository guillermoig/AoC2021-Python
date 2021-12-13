import unittest
from DataReader import DataReader
from PassagePathing import PassagePathing

class TestPassagePathing(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    # def test_getPathDictionaryTest1(self):
    #     data_reader = DataReader("data_test1")
    #     passage_pathing = PassagePathing(data_reader)
    #     self.assertEqual(passage_pathing.path_dictionary, {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'b':['A', 'd', 'end'], 'c': ['A'], 'd': ['b']})

    # def test_getPathDictionaryTest2(self):
    #     data_reader = DataReader("data_test2")
    #     passage_pathing = PassagePathing(data_reader)
    #     self.assertEqual(passage_pathing.path_dictionary, {'dc': ['end', 'HN', 'LN', 'kj'], 'start': ['HN', 'kj', 'dc'], 'HN':['dc', 'end', 'kj'], 'LN': ['dc'], 'kj': ['sa', 'HN', 'dc'], 'sa': ['kj']})

    # def test_getPathDictionaryTest3(self):
    #     data_reader = DataReader("data_test3")
    #     passage_pathing = PassagePathing(data_reader)
    #     self.assertEqual(passage_pathing.path_dictionary, {'fs': ['end', 'he', 'DX', 'pj'], 'he': ['DX', 'fs', 'pj', 'RW', 'WI', 'zg'], 'DX':['he', 'pj', 'fs'], 'start': ['DX', 'pj', 'RW'], 'pj': ['DX', 'zg', 'he', 'RW', 'fs'], 'zg': ['end', 'sl', 'pj', 'RW', 'he'], 'sl': ['zg'], 'RW': ['he', 'pj', 'zg'], 'WI': ['he']})

    def test_getAllPathsTest1(self):
        data_reader = DataReader("data_test1")
        passage_pathing = PassagePathing(data_reader)
        paths_test1 = [
            [['start'],['A'],['b'],['A'],['c'],['A'],['end']],
            [['start'],['A'],['b'],['A'],['end']],
            [['start'],['A'],['b'],['end']],
            [['start'],['A'],['c'],['A'],['b'],['A'],['end']],
            [['start'],['A'],['c'],['A'],['b'],['end']],
            [['start'],['A'],['c'],['A'],['end']],
            [['start'],['A'],['end']],
            [['start'],['b'],['A'],['c'],['A'],['end']],
            [['start'],['b'],['A'],['end']],
            [['start'],['b'],['end']]
        ]
        self.assertEqual(passage_pathing.get_all_paths(), paths_test1)

    # def test_partOne(self):
    #     self.assertEqual(self.passage_pathing.part_one(), 0)

    # def test_partTwo(self):
    #     self.assertEqual(self.passage_pathing.part_two(), 0)

if __name__ == '__main__':
    unittest.main()
