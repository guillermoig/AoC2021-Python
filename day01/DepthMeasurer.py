
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
