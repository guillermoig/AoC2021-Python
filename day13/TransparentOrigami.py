from DataReader import DataReader
from collections import defaultdict
import re
import copy

class TransparentOrigami:
    def __init__(self, data_reader: DataReader) -> None:
        input_data = data_reader.get_all_data().split("\n\n")
        self.map = self.get_dot_positions(input_data[0].splitlines())
        self.instructions = self.get_instructions(input_data[1].splitlines())

    def get_dot_positions(self, dots_data: list) -> list:
        map_data = defaultdict(dict)
        max_rows = 0
        max_columns = 0
        for line in dots_data:
            position = line.split(",")
            max_rows = int(position[1]) if int(position[1]) > max_rows else max_rows
            max_columns = int(position[0]) if int(position[0]) > max_columns else max_columns
            map_data[int(position[1])][int(position[0])] = "#"
        map = [["." for column in range(max_columns + 1)] for row in range(max_rows + 1)]
        for y in map_data:
            for x in map_data[y]:
                map[y][x] = "#"
        return list(map)

    def get_instructions(self, instructions_data: list) -> list:
        instructions = []
        for inst in instructions_data:
            fold_info = re.match("^fold\salong\s(x|y)=([0-9]+)$", inst)
            instructions.append([fold_info[1], fold_info[2]])
        return instructions

    def join_dots(self, char1: str, char2: str) -> str:
        if char1 == '#' or char2 == "#":
            return '#'
        return '.'

    def fold_paper(self, axis: str, line: str) -> None:
        map = []
        new_map = defaultdict(dict)
        if axis == 'x':
            for y in range(len(self.map)):
                for x in range(int(line)):
                    new_map[y][x] = self.join_dots(self.map[y][x], self.map[y][(len(self.map[0]) - 1 - x)])
        else:
            for y in range(int(line)):
                for x in range(len(self.map[0])):
                    new_map[y][x] = self.join_dots(self.map[y][x], self.map[(len(self.map) - 1 - y)][x])
        map = [[new_map[row][column] for column in new_map[row]] for row in new_map]
        self.map = map
        return map

    def part_one(self) -> int:
        self.fold_paper(self.instructions[0][0],self.instructions[0][1])
        count_dots = sum([1 for row in self.map for char in row if char == "#"])
        return count_dots

    def part_two(self) -> int:
        for inst in self.instructions:
            self.fold_paper(inst[0], inst[1])
        str = ''
        for row in self.map:
            str += ''.join(row) + "\n"
        print(str)
        return 0
