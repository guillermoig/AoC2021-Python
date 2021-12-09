from DataReader import DataReader
from SegmentSearcher import SegmentSearcher

def main():
    data_reader = DataReader("data")
    segmentSearcher = SegmentSearcher(data_reader)
    print("Solution to part one: ", segmentSearcher.part_one())
    print("Solution to part two: ", segmentSearcher.part_two())

if __name__ == "__main__":
    main()

