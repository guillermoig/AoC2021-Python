from DataReader import DataReader
from collections import Counter

class SyntaxScoring:
    def __init__(self, data_reader: DataReader) -> None:
        self.map = [[x for x in list(line)] for line in data_reader.get_all_data().splitlines()]

    def part_one(self) -> int:
        return 0

    def part_two(self) -> int:
        return 0
