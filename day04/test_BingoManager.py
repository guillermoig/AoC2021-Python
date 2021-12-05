import unittest
from DataReader import DataReader
from BingoManager import BingoManager

class TestBingoManager(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.bingo_manager = BingoManager(data_reader)
        return super().setUp()

    def test_getRandomNumberList(self):
        self.assertEqual(self.bingo_manager.get_random_number_list(), [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1])

    def test_getNextRandomNumber(self):
        self.assertEqual(self.bingo_manager.get_next_random_number(), 7)

    def test_getRandomNumberProcessedAfterExtractThreeNumber(self):
        for i in range(3):
            number = self.bingo_manager.get_next_random_number()
        self.assertEqual(self.bingo_manager.random_number_processed, [7, 4, 9])

    def test_getRandomNumberListAfterExtractFourNumber(self):
        for i in range(4):
            number = self.bingo_manager.get_next_random_number()
        self.assertEqual(self.bingo_manager.random_number_list, [11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1])

    def test_playATurnAndGetFirstBoard(self):
        self.bingo_manager.play_a_turn(self.bingo_manager.board_list)
        self.assertEqual(self.bingo_manager.board_list[0].get_data(), [[22,13,17,11,0],[8,2,23,4,24],[21,9,14,16,'X'],[6,10,3,18,5],[1,12,20,15,19]])

    def test_playATurnAndGetSecondBoard(self):
        self.bingo_manager.play_a_turn(self.bingo_manager.board_list)
        self.assertEqual(self.bingo_manager.board_list[1].get_data(), [[3,15,0,2,22],[9,18,13,17,5],[19,8,'X',25,23],[20,11,10,24,4],[14,21,16,12,6]])

    def test_playATurnAndGetThirdBoard(self):
        self.bingo_manager.play_a_turn(self.bingo_manager.board_list)
        self.assertEqual(self.bingo_manager.board_list[2].get_data(), [[14,21,17,24,4],[10,16,15,9,19],[18,8,23,26,20],[22,11,13,6,5],[2,0,12,3,'X']])

    def test_partOne(self):
        self.assertEqual(self.bingo_manager.part_one(), 4512)

    def test_partTwo(self):
        self.assertEqual(self.bingo_manager.part_two(), 1924)

if __name__ == '__main__':
    unittest.main()
