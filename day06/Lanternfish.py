from DataReader import DataReader

class Lanternfish:
    def __init__(self, data_reader: DataReader) -> None:
        self.initial_lanternfish_list = [int(x) for x in data_reader.get_all_data().split(",")]
        self.lanternfish_groups = self.initialize_lanternfish_groups()

    def initialize_lanternfish_groups(self) -> list:
        lanternfish_groups = [0 for i in range(9)]
        for i in range(9):
            lanternfish_groups[i] = sum(1 for fish in self.initial_lanternfish_list if fish == i)
        return lanternfish_groups

    def run_a_day(self, lanternfish_list: list) -> list:
        next_lanternfish_list = [0 for i in range(9)]
        next_lanternfish_list[6] = lanternfish_list[0]
        next_lanternfish_list[8] = lanternfish_list[0]
        for index in range(0, len(lanternfish_list)-1):
            next_lanternfish_list[index] += lanternfish_list[index + 1]
        lanternfish_list = next_lanternfish_list
        return lanternfish_list

    def get_evolution_after_n_days(self, days: int) -> list:
        lanternfish_list_evolution = self.lanternfish_groups.copy()
        for day in range(days):
            lanternfish_list_evolution = self.run_a_day(lanternfish_list_evolution)
        return lanternfish_list_evolution

    def part_one(self) -> int:
        lanternfish_list_evolution = self.get_evolution_after_n_days(80)
        return  sum(lanternfish_list_evolution)

    def part_two(self) -> int:
        lanternfish_list_evolution = self.get_evolution_after_n_days(256)
        return  sum(lanternfish_list_evolution)
