from time import process_time_ns
from typing import Callable

from tabulate import tabulate

from brute_force import brute_force
from colony import Colony
from matrix import Matrix


def benchmark(func: Callable):
    t_start = process_time_ns()
    func()
    t_stop = process_time_ns()

    return (t_stop - t_start) / 1e6


def run_benchmark():
    table = []

    for size in range(3, 13, 3):
        print(f'{size=}')
        print(0)
        matrix = Matrix.generate(nodes_count=size)

        print(1)
        brute_force_time = benchmark(lambda: brute_force(matrix))
        print(2)
        ant_time = benchmark(lambda: Colony(path_map=matrix, days=100).find_path())

        table.append([size, brute_force_time, ant_time])
        print(3)

    print(tabulate(
        table, headers=['Размерность', 'Полный перебор, мс', 'Муравьиный алгоритм, мс'], tablefmt='pretty')
    )
