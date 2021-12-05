from DataReader import DataReader
import numpy as np

class Hydrothermal:
    def __init__(self, data_reader: DataReader) -> None:
        raw_data = data_reader.get_all_data().splitlines()
        self.pair_of_points = self.set_pair_of_points(raw_data)
        self.max_number_items = np.amax(self.pair_of_points) + 1

    def set_pair_of_points(self, data) -> list:
        pairs_of_pairs = [line.split(" -> ") for line in data]
        pairs_of_points = [sorted([[int(x) for x in point.split(",")][::-1] for point in pair]) for pair in pairs_of_pairs]
        return sorted(pairs_of_points)

    def get_line_list(self, pair_of_points) -> list:
        line_list = [[0] * self.max_number_items for _ in range(self.max_number_items)]
        for pair in self.pair_of_points:
            if (pair[0][0] != pair[1][0]) and (pair[0][1] != pair[1][1]):
                continue
            y_range = range(pair[0][0], pair[0][0] + 1) if pair[0][0] == pair[1][0] else range(pair[0][0], pair[1][0] + 1)
            x_range = range(pair[0][1], pair[0][1] + 1) if pair[0][1] == pair[1][1] else range(pair[0][1], pair[1][1] + 1)
            for y in y_range:
                for x in x_range:
                    line_list[y][x] += 1
        return line_list

    def part_one(self) -> int:
        line_list = np.array(self.get_line_list(self.pair_of_points))
        return (line_list > 1).sum()

    def part_two(self) -> int:
        return 0
