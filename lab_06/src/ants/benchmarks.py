from time import process_time_ns
from typing import Callable

from tabulate import tabulate

from .brute_force import brute_force
from .colony import Colony
from .matrix import Matrix


class Benchmark:
    def __init__(self, count: int = 3):
        self._count = count

    def _benchmark(self, func: Callable) -> float:
        summary = 0

        for _ in range(self._count):
            t_start = process_time_ns()
            func()
            t_stop = process_time_ns()

            summary += t_stop - t_start

        return round(summary / self._count / 1e6, 3)

    def run(self) -> None:
        table = []

        for size in range(1, 11, 1):
            matrix = Matrix.generate(nodes_count=size)

            brute_force_time = self._benchmark(lambda: brute_force(matrix))
            ant_time = self._benchmark(lambda: Colony(path_map=matrix, days=100).live())

            table.append([size, brute_force_time, ant_time])

        print(tabulate(
            table, headers=['Размерность', 'Полный перебор, мс', 'Муравьиный алгоритм, мс'], tablefmt='pretty')
        )

