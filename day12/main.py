from DataReader import DataReader
from PassagePathing import PassagePathing

def main():
    data_reader = DataReader("data")
    passage_pathing = PassagePathing(data_reader)
    print("Solution to part one: ", passage_pathing.part_one())
    print("Solution to part two: ", passage_pathing.part_two())

if __name__ == "__main__":
    main()

