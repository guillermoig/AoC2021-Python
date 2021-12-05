from BingoManager import BingoManager
from DataReader import DataReader
import re

def main():
    data_reader = DataReader("data")
    bingo_manager = BingoManager(data_reader)
    print("Solution to part one: ", bingo_manager.part_one())
    print("Solution to part two: ", bingo_manager.part_two())

if __name__ == "__main__":
    main()

