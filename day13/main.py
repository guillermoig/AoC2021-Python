from DataReader import DataReader
from TransparentOrigami import TransparentOrigami

def main():
    data_reader = DataReader("data")
    transparent_origami = TransparentOrigami(data_reader)
    print("Solution to part one: ", transparent_origami.part_one())
    print("Solution to part two: ", transparent_origami.part_two())

if __name__ == "__main__":
    main()

