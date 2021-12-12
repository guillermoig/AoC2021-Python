from DataReader import DataReader
from DumboOctopus import DumboOctopus

def main():
    data_reader = DataReader("data")
    dumbo_octopus = DumboOctopus(data_reader)
    print("Solution to part one: ", dumbo_octopus.part_one())
    print("Solution to part two: ", dumbo_octopus.part_two())

if __name__ == "__main__":
    main()

