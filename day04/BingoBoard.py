import re

class BingoBoard:
    def __init__(self, board_data: str) -> None:
        self.data = [[int(x) for x in re.split("\s+", line.strip())] for line in board_data.splitlines()]

    def get_data(self) -> list:
        return self.data

    def cross_out_nummber(self, number) -> None:
        position = [(key, row.index(number)) for (key, row) in enumerate(self.data) if number in row]
        if position:
            self.data[position[0][0]][position[0][1]] = 'X'

    def has_line_completed(self) -> bool:
        for row in self.data:
            if all(item == 'X' for item in row):
                return True
        inverted_data = list(zip(*self.data))
        for row in inverted_data:
            if all(item == 'X' for item in row):
                return True
        return False
