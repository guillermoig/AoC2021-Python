from DataGetter import DataGetter
from Navigator import Navigator
import re

def main():
    data_getter = DataGetter()
    data = data_getter.get_data()
    navigator = Navigator()
    navigator.set_course_instructions(data)
    multiplication = navigator.get_position_multiplication()
    print('Part 1: Position multiplication: ', multiplication)
    # print('Part 2: Number of increases with windows: ', navigator.increases_in_windows_of_three())

if __name__ == "__main__":
    main()

