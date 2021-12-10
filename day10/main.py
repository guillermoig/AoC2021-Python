from DataReader import DataReader
from SyntaxScoring import SyntaxScoring

def main():
    data_reader = DataReader("data")
    syntaxScoring = SyntaxScoring(data_reader)
    print("Solution to part one: ", syntaxScoring.part_one())
    print("Solution to part two: ", syntaxScoring.part_two())

if __name__ == "__main__":
    main()

