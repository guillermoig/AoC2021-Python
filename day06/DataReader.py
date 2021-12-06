import os

class DataReader:
    def __init__(self, filename) -> None:
        challenge_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(challenge_path, filename)

    # Returns all data in the file as unique strin
    def get_all_data(self) -> str:
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    # Returns the first line of data as a list of characters
    def get_first_line(self) -> list:
        with open(self.filename, 'r') as file:
            data = file.readline()
        return list(data)

