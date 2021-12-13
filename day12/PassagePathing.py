from unittest.loader import defaultTestLoader

from networkx.readwrite import graph6
from DataReader import DataReader
import networkx as nx
import matplotlib.pyplot as plt

class PassagePathing:
    def __init__(self, data_reader: DataReader) -> None:
        self.path_dictionary = self.set_path_dictionary(data_reader)
        self.graph = self.set_graph(data_reader)

    def set_graph(self, data_reader: DataReader):
        graph = nx.Graph()
        for line in data_reader.get_all_data().splitlines():
            edge = line.split("-")
            graph.add_edge(edge[0], edge[1])
        # nx.draw(graph, with_labels=True)
        # plt.show()
        return graph

    def set_path_dictionary(self, data_reader) -> dict:
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

    def get_all_paths(self) -> list:
        all_paths = []
        # all_paths = nx.all_shortest_paths(self.graph, source='start', target='end')
        all_simple_paths = nx.all_simple_paths(self.graph, 'start', 'end')
        for path in all_simple_paths:
            all_paths.append(path)
            print(path)
        return all_paths

    def part_one(self) -> int:
        paths = self.get_all_paths()
        return len(paths)

    def part_two(self) -> int:
        return 0
