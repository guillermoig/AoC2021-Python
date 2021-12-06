from DataReader import DataReader
from Lanternfish import Lanternfish

def main():
    data_reader = DataReader("data")
    lanternfish = Lanternfish(data_reader)
    print("Solution to part one: ", lanternfish.part_one())
    print("Solution to part two: ", lanternfish.part_two())

if __name__ == "__main__":
    main()

