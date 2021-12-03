import re

class BinaryDiagnostic:
    def __init__(self, data) -> None:
        self.data = data.splitlines()
        self.data_len = len(self.data)
        self.greatest_number = 2 ** len(self.data[0]) - 1
        pass

    def process_data(self) -> dict:
        processed_data = [0 for i in range(len(self.data[0]))]
        for line in self.data:
            for (key, value) in enumerate(line):
                processed_data[key] += int(value)
        return processed_data

    def get_gamma(self, data) -> int:
        median = self.data_len / 2
        gamma = [int((item - median) > 0) for item in data]
        return (int(''.join([str(item) for item in gamma]), 2))

    def get_epsilon(self, gamma) -> int:
        return gamma ^ self.greatest_number

    def part_one(self):
        processed_data = self.process_data()
        gamma = self.get_gamma(processed_data)
        epsilon = self.get_epsilon(gamma)
        return gamma * epsilon

    def part_two(self):
        return 0
