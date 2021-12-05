from collections import Counter
from DataReader import DataReader
from BingoBoard import BingoBoard
import re

class BingoManager:
    def __init__(self, data_reader: DataReader) -> None:
        raw_data = data_reader.get_all_data().split("\n\n")
        self.random_number_list = [int(x) for x in raw_data.pop(0).split(",")]
        self.random_number_processed = []
        self.board_list = [BingoBoard(board_data) for board_data in raw_data]

    def get_random_number_list(self) -> list:
        return self.random_number_list

    def get_next_random_number(self) -> int:
        next_number = self.random_number_list.pop(0)
        self.random_number_processed.append(next_number)
        return next_number

    def play_a_turn(self, board_list):
        winner_boards = []
        random_number = self.get_next_random_number()
        board_winners = 0
        for board in board_list:
            board.cross_out_nummber(random_number)
            if board.has_line_completed():
                winner_boards.append(board)
        return winner_boards

    def part_one(self) -> int:
        board_list_one = self.board_list.copy()
        winner_boards = []
        while not winner_boards:
            winner_boards = self.play_a_turn(board_list_one)
        items_sum = sum([x for row in winner_boards[0].get_data() for x in row if x != 'X'])
        return items_sum * self.random_number_processed[-1]

    def part_two(self) -> int:
        board_list_two = self.board_list.copy()
        while len(board_list_two) > 0 and len(self.random_number_list) > 0:
            removable_winners = self.play_a_turn(board_list_two)
            if removable_winners:
                winner_board = removable_winners[0]
                for removable_winner in removable_winners:
                    board_list_two.remove(removable_winner)
        items_sum = sum([x for row in winner_board.get_data() for x in row if x != 'X'])
        return items_sum * self.random_number_processed[-1]
