from DataGetter import DataGetter
from Navigator import Navigator
import re

def main():
    data_getter = DataGetter()
    data = data_getter.get_data()
    navigator = Navigator(data)
    print('Part 1: Position multiplication: ', navigator.part_one())
    print('Part 2: Multiplication with aim: ', navigator.part_two())

if __name__ == "__main__":
    main()

