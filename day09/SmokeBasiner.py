from DataReader import DataReader
import operator
import functools as ft

class SmokeBasiner:
    def __init__(self, data_reader: DataReader) -> None:
        self.map = [[int(x) for x in list(line)] for line in data_reader.get_all_data().splitlines()]
        self.y_range = range(len(self.map))
        self.x_range = range(len(self.map[0]))

    def is_low_point(self, index_y, index_x) -> bool:
        low = 0
        max = 0
        if (index_y - 1) in self.y_range:
            max += 1
            if self.map[index_y][index_x] < self.map[index_y - 1][index_x]:
                low += 1
        if (index_y + 1) in self.y_range:
            max += 1
            if self.map[index_y][index_x] < self.map[index_y + 1][index_x]:
                low += 1
        if (index_x - 1) in self.x_range:
            max += 1
            if self.map[index_y][index_x] < self.map[index_y][index_x - 1]:
                low += 1
        if (index_x + 1) in self.x_range:
            max += 1
            if self.map[index_y][index_x] < self.map[index_y][index_x + 1]:
                low += 1
        if low == max:
            return True
        return False

    def part_one(self) -> int:
        low_points = []
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.is_low_point(y, x):
                    low_points.append(self.map[y][x] + 1)
        return sum(low_points)

    def get_basin_points(self, y: int, x: int, prev_basin_points: dict = {}) -> dict:
        basin_points = {} if not prev_basin_points else prev_basin_points
        if self.map[y][x] == 9:
            return {'-'.join([str(y), str(x)]): 'X'}
        basin_points['-'.join([str(y), str(x)])] = self.map[y][x]
        if (y - 1) in self.y_range:
            if '-'.join([str(y-1), str(x)]) not in basin_points:
                basin_points.update(self.get_basin_points(y-1, x, basin_points))
        if (y + 1) in self.y_range:
            if '-'.join([str(y+1), str(x)]) not in basin_points:
                basin_points.update(self.get_basin_points(y+1, x, basin_points))
        if (x - 1) in self.x_range:
            if '-'.join([str(y), str(x-1)]) not in basin_points:
                basin_points.update(self.get_basin_points(y, x-1, basin_points))
        if (x + 1) in self.x_range:
            if '-'.join([str(y), str(x+1)]) not in basin_points:
                basin_points.update(self.get_basin_points(y, x+1, basin_points))
        return basin_points

    def part_two(self) -> int:
        basin_points = []
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.is_low_point(y, x):
                    basin_points_of_y_x = self.get_basin_points(y, x)
                    basin_points.append(sum([1 for x in basin_points_of_y_x.values() if x != 'X']))
        basin_points.sort(reverse=True)
        return ft.reduce(operator.mul, basin_points[:3])
