from DataReader import DataReader
from collections import Counter

class Positioner:
    def __init__(self, data_reader: DataReader) -> None:
        self.raw_data = [int(x) for x in data_reader.get_first_line().splitlines()[0].split(",")]
        self.min_value = min(self.raw_data)
        self.max_value = max(self.raw_data)
        self.positions_dict = self.set_positions_dict()
        self.factor_list = self.get_factor_list()

    def set_positions_dict(self) -> dict:
        positions_dict = {key:0 for key in range(self.min_value, self.max_value + 1)}
        positions_dict.update(Counter(self.raw_data))
        return positions_dict

    def get_factor_list(self) -> dict:
        factor_list = {key:0 for key in range(self.max_value + 1)}
        for key, value in factor_list.items():
            for factor in range (key + 1):
                factor_list[key] += factor
        return factor_list

    def get_spent_fuel(self) -> dict:
        spent_fuel_dict = {key:0 for key in range(self.min_value, self.max_value + 1)}
        for key, value in self.positions_dict.items():
            for inner_key, inner_value in self.positions_dict.items():
                spent_fuel_dict[key] += abs(inner_key - key) * int(inner_value)
        return spent_fuel_dict

    def part_one(self) -> int:
        spent_fuel = self.get_spent_fuel()
        return min(spent_fuel.values())

    def get_spent_fuel_expensive(self) -> dict:
        spent_fuel_dict = {key:0 for key in range(self.min_value, self.max_value + 1)}
        for key, value in self.positions_dict.items():
            for inner_key, inner_value in self.positions_dict.items():
                difference = abs(inner_key - key)
                spent_fuel_dict[key] += self.factor_list[difference] * int(inner_value)
        return spent_fuel_dict

    def part_two(self) -> int:
        spent_fuel = self.get_spent_fuel_expensive()
        return min(spent_fuel.values())
