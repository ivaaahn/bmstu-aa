from copy import deepcopy

import consts

from ant import Ant
from matrix import MatrixType, Matrix


class Colony:
    PHEROMONE_RATIO = consts.PHEROMONE_RATIO

    def __init__(self, path_map: MatrixType, days: int, alpha: float = consts.ALPHA, beta: float = consts.BETA, p: float = consts.P):
        self.alpha = alpha
        self.beta = beta
        self.p = p

        self._path_map = path_map
        self._days = days
        self._ph_map = Matrix.create(len(path_map), self.PHEROMONE_RATIO)
        self._nodes = [_ for _ in range(len(self._path_map))]
        self._q_ratio = sum([sum(row) for row in self._path_map], 0) / 2 / len(self._nodes)
        self._ants = [Ant(colony=self, pos=node) for node in self._nodes]
        self._shortest_path: tuple[int, list[int]] = (consts.MAX_INT, [])

    def _live_day(self) -> None:
        """Обновляет каждый день самый коротки путь за день и его длину"""
        for ant in self._ants:
            curr_dist, curr_path = ant.go()

            if curr_dist < self._shortest_path[0]:
                self._shortest_path = curr_dist, deepcopy(curr_path)

    def _update_pheromones(self):
        for ant in self._ants:
            ant.update_pheromone()

    def live(self) -> tuple[int, list[int]]:
        for _ in range(self._days):
            self._live_day()
            self._update_pheromones()

        return self._shortest_path
