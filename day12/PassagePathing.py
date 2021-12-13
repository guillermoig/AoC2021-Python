from unittest.loader import defaultTestLoader
from DataReader import DataReader

class PassagePathing:
    def __init__(self, data_reader: DataReader) -> None:
        self.nodes_edges = self.set_nodes_edges(data_reader)
        self.lower_nodes = [char for char in self.nodes_edges if char.islower() and char != 'start']

    def set_nodes_edges(self, data_reader) -> dict:
        path_dict = {}
        for line in data_reader.get_all_data().splitlines():
            source = line.split("-")[0]
            destination = line.split("-")[1]
            if source != 'end' and destination != 'start':
                if source in path_dict:
                    path_dict[source].append(destination)
                else:
                    path_dict[source] = [destination]
            if source != 'start' and destination != 'end':
                if destination in path_dict:
                    path_dict[destination].append(source)
                else:
                    path_dict[destination] = [source]
        return path_dict

    def get_all_paths_part_one(self, source: str, destination: str, prev_nodes_visited: dict = {}) -> list:
        nodes_visited = prev_nodes_visited.copy()
        if source == destination:
            return [[destination]]
        paths = []
        nodes_visited[source] = 1 if source not in nodes_visited else nodes_visited[source] + 1
        for value in self.nodes_edges[source]:
            if value in nodes_visited and nodes_visited[value] == 1 and value in self.lower_nodes:
                continue
            sub_paths = self.get_all_paths_part_one(value, destination, nodes_visited)
            for path in sub_paths:
                new_path = [source] + path
                paths.append(new_path)
        return paths

    def part_one(self) -> int:
        paths = self.get_all_paths_part_one('start', 'end')
        return len(paths)

    def has_lower_repeated(self, value: str, nodes_visited: dict) -> bool:
        for node in nodes_visited:
            if node in self.lower_nodes and node != value and nodes_visited[node] == 2:
                return True
        return False

    def get_all_paths_part_two(self, source: str, destination: str, prev_nodes_visited: dict = {}) -> list:
        nodes_visited = prev_nodes_visited.copy()
        if source == destination:
            return [[destination]]
        paths = []
        nodes_visited[source] = 1 if source not in nodes_visited else nodes_visited[source] + 1
        for value in self.nodes_edges[source]:
            if value in nodes_visited and value in self.lower_nodes and (nodes_visited[value] == 2 or self.has_lower_repeated(value, nodes_visited)):
                continue
            sub_paths = self.get_all_paths_part_two(value, destination, nodes_visited)
            for path in sub_paths:
                new_path = [source] + path
                paths.append(new_path)
        return paths

    def part_two(self) -> int:
        paths = self.get_all_paths_part_two('start', 'end')
        return len(paths)
