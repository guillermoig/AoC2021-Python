import unittest
from BingoBoard import BingoBoard

class TestBingoBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.bingo_board = BingoBoard("22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19")
        return super().setUp()

    def test_getData(self):
        self.assertEqual(self.bingo_board.get_data(), [[22,13,17,11,0],[8,2,23,4,24],[21,9,14,16,7],[6,10,3,18,5],[1,12,20,15,19]])

    def test_crossOutNumber(self):
        self.bingo_board.cross_out_nummber(22)
        self.bingo_board.cross_out_nummber(18)
        self.bingo_board.cross_out_nummber(12)
        self.bingo_board.cross_out_nummber(54)
        self.assertEqual(self.bingo_board.get_data(), [['X',13,17,11,0],[8,2,23,4,24],[21,9,14,16,7],[6,10,3,'X',5],[1,'X',20,15,19]])

    def test_hasLineCompletedRow(self):
        self.bingo_board.cross_out_nummber(22)
        self.bingo_board.cross_out_nummber(13)
        self.bingo_board.cross_out_nummber(17)
        self.bingo_board.cross_out_nummber(11)
        self.bingo_board.cross_out_nummber(0)
        self.assertEqual(self.bingo_board.has_line_completed(), True)

    def test_hasLineCompletedColumn(self):
        self.bingo_board.cross_out_nummber(0)
        self.bingo_board.cross_out_nummber(24)
        self.bingo_board.cross_out_nummber(7)
        self.bingo_board.cross_out_nummber(5)
        self.bingo_board.cross_out_nummber(19)
        self.assertEqual(self.bingo_board.has_line_completed(), True)

if __name__ == '__main__':
    unittest.main()
