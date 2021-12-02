import os

class DataGetter:
    def __init__(self) -> None:
        challenge_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(challenge_path, 'data')

    def get_data(self) -> list:
        file = open(self.filename, 'r')
        data = file.read()
        file.close()
        return data

