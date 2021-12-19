import typing
from random import random

import consts
from matrix import Matrix, MatrixType

if typing.TYPE_CHECKING:
    from colony import Colony


class Ant:
    def __init__(self, colony: 'Colony', pos: int):
        self._colony = colony
        self._visited = [pos]
        self._curr_pos = pos
        self._path = Matrix.create(len(colony._path_map), initial_value=False)

    @property
    def q_ratio(self) -> int:
        return self._colony._q_ratio

    @property
    def nodes(self) -> list[int]:
        return self._colony._nodes

    @property
    def paths_map(self) -> MatrixType:
        return self._colony._path_map

    @property
    def ph_map(self) -> MatrixType:
        return self._colony._ph_map

    def _get_probability(self) -> dict:
        paths_probability = {}
        total_probability = 0

        src = self._curr_pos
        for dst, distance in enumerate(self.paths_map[src]):
            if dst in self._visited:
                continue

            curr = pow(self.ph_map[src][dst], self._colony.alpha) * pow(1 / distance, self._colony.beta) if distance else 0
            paths_probability[dst] = curr
            total_probability += curr

        return {k_old: v_old / (total_probability or 1) for k_old, v_old in paths_probability.items()}

    def update_pheromone(self):
        ph_map, paths_map, visited = self.ph_map, self.paths_map, self._visited

        dist, path = self.get_result()

        delta = self.q_ratio / dist if dist else 0

        for node_1 in self.nodes:
            for node_2, old_value in enumerate(self.ph_map[node_1]):
                curr_delta = 0
                if paths_map[node_1][node_2]:
                    passed = False
                    for k in range(len(visited)):
                        src, dst = visited[k], visited[(k + 1) % len(visited)]
                        if passed := (src == node_1 and dst == node_2) or (dst == node_1 and src == node_2):
                            break

                    curr_delta = delta if passed else 0

                ph_map[node_1][node_2] = (1 - self._colony.p) * (old_value + curr_delta)

                if ph_map[node_1][node_2] <= 0:
                    ph_map[node_1][node_2] = consts.BASE_PHEROMONE

    def _move(self, new_pos: int):
        self._path[self._curr_pos][new_pos] = True
        self._curr_pos = new_pos

        self._visited.append(self._curr_pos)

    def _choose_position(self) -> typing.Optional[int]:
        probs = self._get_probability()

        choice = random()
        total = 0
        for k, v in probs.items():
            if total <= choice < total + v:
                return k

            total += v

        return None

    def get_result(self) -> tuple[int, list[int]]:
        path, path_len = self._visited, len(self._visited)
        path_map = self.paths_map
        return sum([path_map[path[i]][path[(i + 1) % path_len]] for i in range(path_len)]), path

    def go(self):
        while (new_pos := self._choose_position()) is not None:
            self._move(new_pos)

        return self.get_result()
