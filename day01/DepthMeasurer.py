
class DepthMeasurer:
    def __init__(self) -> None:
        pass

    def set_measures(self, measures) -> None:
        self.measures = list(int(number) for number in measures.splitlines())

    def get_measures(self) -> list:
        return self.measures

    def increases_counter(self) -> int:
        counter = 0
        for x,y in zip(self.measures[::],self.measures[1::]):
            if x < y:
                counter += 1
        return counter

    def group_by_window(self, window_size) -> list:
        grouped_data = [sum(self.measures[i:i+window_size]) for i in range(0, len(self.measures), 1) if len(self.measures) >= i + window_size]
        return grouped_data

    def increases_in_windows_of_three(self) -> int:
        self.measures = self.group_by_window(3)
        return self.increases_counter()
