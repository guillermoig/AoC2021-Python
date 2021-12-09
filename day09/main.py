from DataReader import DataReader
from SmokeBasiner import SmokeBasiner

def main():
    data_reader = DataReader("data")
    smokeBasiner = SmokeBasiner(data_reader)
    print("Solution to part one: ", smokeBasiner.part_one())
    print("Solution to part two: ", smokeBasiner.part_two())

if __name__ == "__main__":
    main()

