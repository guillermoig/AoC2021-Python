from Hydrothermal import Hydrothermal
from DataReader import DataReader
import re

def main():
    data_reader = DataReader("data")
    hydrothermal = Hydrothermal(data_reader)
    print("Solution to part one: ", hydrothermal.part_one())
    print("Solution to part two: ", hydrothermal.part_two())

if __name__ == "__main__":
    main()

