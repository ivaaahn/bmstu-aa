import sys
import typing
from copy import deepcopy
from random import random

import consts

from matrix import Matrix, MatrixType

if typing.TYPE_CHECKING:
    from colony import Colony


class Ant:
    def __init__(self, colony: 'Colony', pos: int):
        self.colony = colony
        self.visited = [pos]
        self.curr_pos = pos
        self.path = Matrix.create(len(colony.path_map), initial_value=False)

    @property
    def q_ratio(self) -> int:
        return self.colony.q_ratio

    @property
    def nodes(self) -> list[int]:
        return self.colony.nodes

    def allowed_nodes_from(self, v: int) -> list[int]:
        return list(set(self.paths_map[v]) - set(self.visited))

    @property
    def paths_map(self) -> MatrixType:
        return self.colony.path_map

    @property
    def ph_map(self) -> MatrixType:
        return self.colony.ph_map

    def get_probability(self) -> dict:
        paths_probability = {}
        total_probability = 0

        src = self.curr_pos
        for dst, distance in enumerate(self.paths_map[src]):
            if dst in self.visited:
                continue

            curr = pow(self.ph_map[src][dst], consts.ALPHA * pow(1 / distance, consts.BETA)) if distance else 0
            paths_probability[dst] = curr
            total_probability += curr

        return {k_old: v_old / (total_probability or 1) for k_old, v_old in paths_probability.items()}

    def update_pheromone(self):
        print('update_pheromone')
        ph_map = self.ph_map
        paths_map = self.paths_map

        for src in self.nodes:
            for dst, old_value in enumerate(ph_map[src]):
                if paths_map[src][dst] != 0:
                    delta = self.q_ratio / paths_map[src][dst] if self.path[src][dst] else 0
                    ph_map[src][dst] = (1 - consts.P) * (old_value + delta)

                if ph_map[src][dst] <= 0:
                    ph_map[src][dst] = consts.BASE_PHEROMONE

    def move(self, new_pos: int):
        print('move')

        self.path[self.curr_pos][new_pos] = True
        self.curr_pos = new_pos

        self.visited.append(self.curr_pos)

    def choose_position(self) -> typing.Optional[int]:
        probs = self.get_probability()

        choice = random()
        total = 0
        for k, v in probs.items():
            if total <= choice < total + v:
                return k

            total += v

        return None

    def get_result(self) -> tuple[int, list[int]]:
        path, path_len = self.visited, len(self.visited)
        path_map = self.paths_map
        return sum([path_map[path[i]][path[(i + 1) % path_len]] for i in range(path_len)]), path

    def go(self):
        while (new_pos := self.choose_position()) is not None:
            self.move(new_pos)
            self.update_pheromone()
