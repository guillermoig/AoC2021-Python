from DataReader import DataReader
from Positioner import Positioner

def main():
    data_reader = DataReader("data")
    positioner = Positioner(data_reader)
    print("Solution to part one: ", positioner.part_one())
    print("Solution to part two: ", positioner.part_two())

if __name__ == "__main__":
    main()

