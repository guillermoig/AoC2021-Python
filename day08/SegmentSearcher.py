from DataReader import DataReader
from collections import Counter

class SegmentSearcher:
    def __init__(self, data_reader: DataReader) -> None:
        self.number_segment_count = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
        self.raw_data = data_reader.get_all_data().splitlines()
        self.get_data_input_output()

    def get_data_input_output(self) -> list:
        input = []
        output = []
        for line in self.raw_data:
            data = line.split(" | ")
            input.append(data[0].split(" "))
            output.append(data[1].split(" "))
        self.data_input = input
        self.data_output = output

    def part_one(self) -> int:
        defined_numbers_counter = sum([1 for sublist in self.data_output for item in sublist if len(item) in [2, 3, 4, 7]])
        return defined_numbers_counter

    def get_known_numbers(self, input: list) -> dict:
        known_numbers = {}
        for x in input:
            if len(x) == 2:
                known_numbers[1] = sorted(list(x))
            elif len(x) == 4:
                known_numbers[4] = sorted(list(x))
            elif len(x) == 3:
                known_numbers[7] = sorted(list(x))
            elif len(x) == 7:
                known_numbers[8] = sorted(list(x))
        return known_numbers

    def get_segment_0(self, known_numbers: dict) -> str:
        char = [char for char in known_numbers[7] if char not in known_numbers[1]]
        return char[0]

    def get_segment_6(self, known_numbers: dict, segment_letter: dict, input: list) -> str:
        segments_in_4_ext = known_numbers[4]
        segments_in_4_ext.append(segment_letter[0])
        for number in input:
            if len(number) == 6:
                difference = [char for char in number if char not in segments_in_4_ext]
                if len(difference) == 1:
                    return difference[0]
        return ''

    def get_segment_4(self, known_numbers: dict) -> str:
        char = [char for char in known_numbers[8] if char not in known_numbers[9]]
        return char[0]

    def get_segment_2(self, known_numbers: dict, input: list) -> str:
        for number in input:
            if len(number) == 6:
                char = [char for char in known_numbers[1] if char not in number]
                if len(char) == 1:
                    return char[0]
        return ''

    def get_segment_5(self, known_numbers: dict, segment_2: str) -> str:
        return [char for char in known_numbers[1] if char not in [segment_2]][0]

    def get_segment_3(self, segment_letter: dict, input: list) -> str:
        segment_to_compare = [segment_letter[0], segment_letter[2], segment_letter[4], segment_letter[6]]
        for number in input:
            if len(number) == 5:
                char = [char for char in number if char not in segment_to_compare]
                if len(char) == 1:
                    return char[0]
        return ''

    def get_segment_1(self, segment_letter: dict, letters_of_8: list) -> str:
        return [char for char in letters_of_8 if char not in sorted(segment_letter.values())][0]

    def name_segments(self, input: list) -> dict:
        segment_letter = {}
        known_numbers = self.get_known_numbers(input)
        segment_letter[0] = self.get_segment_0(known_numbers)
        segment_letter[6] = self.get_segment_6(known_numbers, segment_letter, input)
        known_numbers[9] = list(dict.fromkeys(known_numbers[4] + known_numbers[7] + [segment_letter[6]]))
        segment_letter[4] = self.get_segment_4(known_numbers)
        segment_letter[2] = self.get_segment_2(known_numbers, input)
        segment_letter[5] = self.get_segment_5(known_numbers, segment_letter[2])
        segment_letter[3] = self.get_segment_3(segment_letter, input)
        segment_letter[1] = self.get_segment_1(segment_letter, known_numbers[8])
        return segment_letter

    def get_numbers_in_segments(self, named_segments: dict) -> dict:
        number_in_segments = {}
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,1,2,4,5,6]]))] = '0'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [2,5]]))] = '1'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,2,3,4,6]]))] = '2'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,2,3,5,6]]))] = '3'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [1,2,3,5]]))] = '4'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,1,3,5,6]]))] = '5'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,1,3,4,5,6]]))] = '6'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,2,5]]))] = '7'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,1,2,3,4,5,6]]))] = '8'
        number_in_segments[''.join(sorted([named_segments[segment] for segment in [0,1,2,3,5,6]]))] = '9'
        # number_in_segments[0] = [named_segments[segment] for segment in [0,1,2,4,5,6]]
        # number_in_segments[1] = [named_segments[segment] for segment in [2,5]]
        # number_in_segments[2] = [named_segments[segment] for segment in [0,2,3,4,6]]
        # number_in_segments[3] = [named_segments[segment] for segment in [0,2,3,5,6]]
        # number_in_segments[4] = [named_segments[segment] for segment in [1,2,3,5]]
        # number_in_segments[5] = [named_segments[segment] for segment in [0,1,3,5,6]]
        # number_in_segments[6] = [named_segments[segment] for segment in [0,1,3,4,5,6]]
        # number_in_segments[7] = [named_segments[segment] for segment in [0,2,5]]
        # number_in_segments[8] = [named_segments[segment] for segment in [0,1,2,3,4,5,6]]
        # number_in_segments[9] = [named_segments[segment] for segment in [0,1,2,3,5,6]]
        return number_in_segments

    def decode_input(self, input: list) -> list:
        number_in_segments = []
        input_split = [list(x) for x in input]
        named_segments = self.name_segments(input_split)
        number_in_segments = self.get_numbers_in_segments(named_segments)
        return number_in_segments

    def decode_output(self, input_decoded: list, output: list) -> int:
        decoded_output = ''
        for number in output:
            ordered_letters = ''.join(sorted(number))
            decoded_output += input_decoded[''.join(sorted(number))]
        return int(decoded_output)

    def decode_output_numbers(self) -> dict:
        decoded_numbers = {}
        for key, input in enumerate(self.data_input):
            input_decoded = self.decode_input(input)
            decoded_numbers[key] = self.decode_output(input_decoded, self.data_output[key])
        return decoded_numbers

    def part_two(self) -> int:
        output_numbers_decoded = self.decode_output_numbers()
        return sum(output_numbers_decoded.values())
