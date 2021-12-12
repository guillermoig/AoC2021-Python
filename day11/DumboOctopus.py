from DataReader import DataReader
import copy

class DumboOctopus:
    def __init__(self, data_reader: DataReader) -> None:
        self.map = [[int(x) for x in list(line)] for line in data_reader.get_all_data().splitlines()]

    def get_close_flashes(self, map: list, row: int, column: int) -> int:
        close_flashing = 0
        row_low_limit = 0 if (row == 0) else row - 1
        row_high_limit = len(map) if (row > len(map) - 2) else row + 2
        column_low_limit = 0 if (column == 0) else column - 1
        column_high_limit = len(map[0]) if (column > len(map[0]) - 2) else column + 2
        for y in range(row_low_limit, row_high_limit):
            for x in range(column_low_limit, column_high_limit):
                if (y == row) and (x == column):
                    continue
                if map[y][x] == 11:
                    close_flashing += 1
        return close_flashing

    def process_flashes(self, map_to_process: list) -> list:
        map_prev = []
        map_processed = copy.deepcopy(map_to_process)
        while map_prev != map_processed:
            map_processed = [[11 if x == 10 else x for x in row] for row in map_processed]
            map_prev = copy.deepcopy(map_processed)
            for row in range(len(map_prev)):
                for column in range(len(map_prev[row])):
                    if map_processed[row][column] < 10:
                        map_processed[row][column] += self.get_close_flashes(map_prev, row, column)
                        if map_processed[row][column] > 9:
                            map_processed[row][column] = 10
            map_processed = [[12 if x == 11 else x for x in row] for row in map_processed]
        map_processed = [[0 if x > 10 else x for x in row ] for row in map_processed]
        return map_processed


    def run_step(self) -> None:
        # First add 1 to every element
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                self.map[row][column] += 1
        # Check those that flash
        self.map = self.process_flashes(self.map.copy())
        return self.map

    def get_flashes(self) -> int:
        return sum([1 for row in self.map for column in row if column == 0])

    def get_total_flashes(self, steps: int) -> int:
        total = 0
        for i in range(steps):
            self.run_step()
            total += self.get_flashes()
        return total

    def part_one(self) -> int:
        return self.get_total_flashes(100)

    def part_two(self) -> int:
        step_synchronized = 0
        map_all_flash = self.get_flashes()
        total_octopus = len(self.map) * len(self.map[0])
        while map_all_flash < total_octopus:
            step_synchronized += 1
            self.run_step()
            map_all_flash = self.get_flashes()
        return step_synchronized
