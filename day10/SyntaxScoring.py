from DataReader import DataReader
from collections import Counter

class SyntaxScoring:
    def __init__(self, data_reader: DataReader) -> None:
        self.map = [[x for x in list(line)] for line in data_reader.get_all_data().splitlines()]
        self.score_table_part_one = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.score_table_part_two = {')': 1, ']': 2, '}': 3, '>': 4}
        self.open_close_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def get_wrong_character(self, line: list) -> str:
        wrong_char = ''
        open_sequence = []
        for char in line:
            if char in self.open_close_chars.keys():
                open_sequence.append(char)
                continue
            if not open_sequence or char != self.open_close_chars[open_sequence.pop(-1)]:
                wrong_char = char
                break
        return wrong_char

    def part_one(self) -> int:
        error_by_line = []
        for line in self.map:
            error_by_line.append(self.get_wrong_character(line))
        error_total = dict(Counter(error_by_line))
        return sum([counter * self.score_table_part_one[char] for char, counter in error_total.items() if char != ''])

    def get_incomplete_lines(self) -> list:
        incomplete_lines = []
        for line in self.map:
            wrong_character = self.get_wrong_character(line)
            if not wrong_character:
                incomplete_lines.append(line)
        return incomplete_lines

    def get_close_chars_list(self, line: list) -> str:
        open_sequence = []
        for char in line:
            if char in self.open_close_chars.keys():
                open_sequence.append(char)
                continue
            if open_sequence:
                if char != self.open_close_chars[open_sequence[-1]]:
                    break
                open_sequence = open_sequence[:-1]
        close_sequence = [self.open_close_chars[char] for char in open_sequence]
        close_sequence.reverse()
        return close_sequence

    def part_two(self) -> int:
        total_by_line = []
        incomplete_lines = self.get_incomplete_lines()
        for line in incomplete_lines:
            close_chars = self.get_close_chars_list(line)
            total = 0
            for char in close_chars:
                total = 5 * total + self.score_table_part_two[char]
            total_by_line.append(total)
        total_by_line.sort()
        return total_by_line[int(len(total_by_line) / 2)]
