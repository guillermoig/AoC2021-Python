from collections import Counter

class BinaryDiagnostic:
    def __init__(self, data) -> None:
        self.data = [list(line) for line in data.splitlines()]
        self.data_len = len(self.data)
        self.greatest_number = 2 ** len(self.data[0]) - 1

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

    def get_bits_counter(self, items, position) -> tuple:
        values = [item[position] for item in items]
        bits_counter = Counter(values).most_common(2)
        return bits_counter

    def get_oxygen_generator_rating(self) -> int:
        reduced_data = self.data.copy()
        index = 0
        while len(reduced_data) > 1:
            bits_counter = self.get_bits_counter(reduced_data, index)
            if bits_counter[0][1] == bits_counter[1][1]:
                most_repeated_value = 1
            else:
                most_repeated_value = int(bits_counter[0][0])
            reduced_data = [row for row in reduced_data if str(most_repeated_value) in row[index]]
            index += 1
        return (int(''.join([str(item) for item in reduced_data[0]]), 2))

    def get_co2_scrubber_rating(self) -> int:
        reduced_data = self.data.copy()
        index = 0
        while len(reduced_data) > 1:
            bits_counter = self.get_bits_counter(reduced_data, index)
            if bits_counter[0][1] == bits_counter[1][1]:
                most_repeated_value = 0
            else:
                most_repeated_value = int(bits_counter[1][0])
            reduced_data = [row for row in reduced_data if str(most_repeated_value) in row[index]]
            index += 1
        return (int(''.join([str(item) for item in reduced_data[0]]), 2))

    def part_two(self):
        oxygen_generator_rating = self.get_oxygen_generator_rating()
        co2_scrubber_rating = self.get_co2_scrubber_rating()
        return oxygen_generator_rating * co2_scrubber_rating
