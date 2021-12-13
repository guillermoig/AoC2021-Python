import unittest
from DataReader import DataReader
from PassagePathing import PassagePathing

class TestPassagePathing(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_getNodesEdgesTest1(self):
        data_reader = DataReader("data_test1")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.nodes_edges, {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'b':['A', 'd', 'end'], 'c': ['A'], 'd': ['b']})

    def test_getNodesEdgesTest2(self):
        data_reader = DataReader("data_test2")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.nodes_edges, {'dc': ['end', 'HN', 'LN', 'kj'], 'start': ['HN', 'kj', 'dc'], 'HN':['dc', 'end', 'kj'], 'LN': ['dc'], 'kj': ['sa', 'HN', 'dc'], 'sa': ['kj']})

    def test_getNodesEdgesTest3(self):
        data_reader = DataReader("data_test3")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.nodes_edges, {'fs': ['end', 'he', 'DX', 'pj'], 'he': ['DX', 'fs', 'pj', 'RW', 'WI', 'zg'], 'DX':['he', 'pj', 'fs'], 'start': ['DX', 'pj', 'RW'], 'pj': ['DX', 'zg', 'he', 'RW', 'fs'], 'zg': ['end', 'sl', 'pj', 'RW', 'he'], 'sl': ['zg'], 'RW': ['he', 'pj', 'zg'], 'WI': ['he']})

    def test_getLowerNodesTest1(self):
        data_reader = DataReader("data_test1")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.lower_nodes, ['c', 'b', 'd'])

    def test_getLowerNodesTest2(self):
        data_reader = DataReader("data_test2")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.lower_nodes, ['dc', 'kj', 'sa'])

    def test_getLowerNodesTest3(self):
        data_reader = DataReader("data_test3")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.lower_nodes, ['fs', 'he', 'pj', 'zg', 'sl'])

    def test_getAllPathsTest1(self):
        data_reader = DataReader("data_test1")
        passage_pathing = PassagePathing(data_reader)
        paths_test1 = [
            ['start', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'end'],
            ['start', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'end'],
            ['start', 'b', 'end']
        ]
        self.assertEqual(passage_pathing.get_all_paths_part_one('start', 'end'), paths_test1)

    def test_getAllPathsTest2(self):
        data_reader = DataReader("data_test2")
        passage_pathing = PassagePathing(data_reader)
        paths_test2 = [
            ['start', 'HN', 'dc', 'end'],
            ['start', 'HN', 'dc', 'HN', 'end'],
            ['start', 'HN', 'dc', 'HN', 'kj', 'HN', 'end'],
            ['start', 'HN', 'dc', 'kj', 'HN', 'end'],
            ['start', 'HN', 'end'],
            ['start', 'HN', 'kj', 'HN', 'dc', 'end'],
            ['start', 'HN', 'kj', 'HN', 'dc', 'HN', 'end'],
            ['start', 'HN', 'kj', 'HN', 'end'],
            ['start', 'HN', 'kj', 'dc', 'end'],
            ['start', 'HN', 'kj', 'dc', 'HN', 'end'],
            ['start', 'kj', 'HN', 'dc', 'end'],
            ['start', 'kj', 'HN', 'dc', 'HN', 'end'],
            ['start', 'kj', 'HN', 'end'],
            ['start', 'kj', 'dc', 'end'],
            ['start', 'kj', 'dc', 'HN', 'end'],
            ['start', 'dc', 'end'],
            ['start', 'dc', 'HN', 'end'],
            ['start', 'dc', 'HN', 'kj', 'HN', 'end'],
            ['start', 'dc', 'kj', 'HN', 'end']
        ]
        self.assertEqual(passage_pathing.get_all_paths_part_one('start', 'end'), paths_test2)

    def test_partOneTest1(self):
        data_reader = DataReader("data_test1")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.part_one(), 10)

    def test_partOneTest2(self):
        data_reader = DataReader("data_test2")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.part_one(), 19)

    def test_partOneTest3(self):
        data_reader = DataReader("data_test3")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.part_one(), 226)

    def test_getAllPathsTest1PartTwo(self):
        data_reader = DataReader("data_test1")
        passage_pathing = PassagePathing(data_reader)
        paths_test1 = [
            ['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'd', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'end'],
            ['start', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'end'],
            ['start', 'A', 'b', 'end'],
            ['start', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'end'],
            ['start', 'b', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'end'],
            ['start', 'b', 'end']
        ]
        self.assertEqual(passage_pathing.get_all_paths_part_two('start', 'end'), paths_test1)

    def test_partTwoTest1(self):
        data_reader = DataReader("data_test1")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.part_two(), 36)

    def test_partTwoTest2(self):
        data_reader = DataReader("data_test2")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.part_two(), 103)

    def test_partTwoTest3(self):
        data_reader = DataReader("data_test3")
        passage_pathing = PassagePathing(data_reader)
        self.assertEqual(passage_pathing.part_two(), 3509)

if __name__ == '__main__':
    unittest.main()
