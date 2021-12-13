import unittest
from DataReader import DataReader
from TransparentOrigami import TransparentOrigami

class TestTransparentOrigami(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.transparent_origami = TransparentOrigami(data_reader)
        return super().setUp()

    def test_getDotPositions(self):
        map_str = "...#..#..#.\n....#......\n...........\n#..........\n...#....#.#\n...........\n...........\n...........\n...........\n...........\n.#....#.##.\n....#......\n......#...#\n#..........\n#.#........"
        map = [list(row) for row in map_str.splitlines()]
        self.assertEqual(self.transparent_origami.map, map)

    def test_foldPaper1Time(self):
        map_str = "#.##..#..#.\n#...#......\n......#...#\n#...#......\n.#.#..#.###\n...........\n..........."
        map = [list(row) for row in map_str.splitlines()]
        self.assertEqual(self.transparent_origami.fold_paper('y', '7'), map)

    def test_foldPaper2Times(self):
        map_str = "#####\n#...#\n#...#\n#...#\n#####\n.....\n....."
        map = [list(row) for row in map_str.splitlines()]
        self.transparent_origami.fold_paper('y', '7')
        self.assertEqual(self.transparent_origami.fold_paper('x', '5'), map)

    def test_partOne(self):
        self.assertEqual(self.transparent_origami.part_one(), 17)

    def test_partTwo(self):
        self.assertEqual(self.transparent_origami.part_two(), 0)

if __name__ == '__main__':
    unittest.main()
