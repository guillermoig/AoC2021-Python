from DataReader import DataReader
from BinaryDiagnostic import BinaryDiagnostic
import re

def main():
    data_reader = DataReader()
    data = data_reader.get_all_data()
    binary_diagnostic = BinaryDiagnostic(data)
    print("Solution to part one: ", binary_diagnostic.part_one())
    print("Solution to part two: ", binary_diagnostic.part_two())

if __name__ == "__main__":
    main()

