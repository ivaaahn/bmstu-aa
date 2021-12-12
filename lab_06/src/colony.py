from copy import deepcopy

import consts

from ant import Ant
from matrix import MatrixType, Matrix


class Colony:
    PHEROMONE_RATIO = consts.PHEROMONE_RATIO

    def __init__(self, path_map: MatrixType, days: int):
        self.path_map = path_map
        self.days = days
        self.ph_map = Matrix.create(len(path_map), self.PHEROMONE_RATIO)
        self.nodes = [_ for _ in range(len(self.path_map))]
        self.q_ratio = sum([sum(row) for row in self.path_map], 0) / 2 / len(self.nodes)
        print(self.q_ratio)

    def find_path(self):
        shortest_length = consts.MAX_INT
        shortest_path = []

        for _ in range(self.days):
            for node_i in self.nodes:
                ant = Ant(colony=self, pos=node_i)
                ant.go()
                curr_dist, curr_path = ant.get_result()

                if shortest_length > curr_dist:
                    shortest_length = curr_dist
                    shortest_path = deepcopy(curr_path)

        return shortest_length, shortest_path
