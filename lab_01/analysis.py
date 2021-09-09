import string
import random
import time

import matplotlib.pyplot as plt

from typing import Optional
from timeit import timeit
from time import process_time_ns

from lib import LevenshteinFunc, func_description as levenshtein_func_description
from lib import (
    levenshtein_recurs,
    levenshtein_recurs_mem,
    damerau_levenshtein,
    damerau_levenshtein_recurs,
)


class Analyzer:
    _REPEATS = 10
    _FUNCS: dict[LevenshteinFunc, str] = levenshtein_func_description
    _RESULTS: dict[LevenshteinFunc, dict[int, int]] = dict()
    _LENGTHS: dict[LevenshteinFunc, list[int]] = {
        levenshtein_recurs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        levenshtein_recurs_mem: [0, 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500],
        damerau_levenshtein: [0, 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500],
        damerau_levenshtein_recurs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }

    @classmethod
    def start(cls) -> None:
        for f in cls._FUNCS:
            print(f'{cls._FUNCS[f]} get started')
            cls._RESULTS[f] = {length: cls._test_function(f, cls._REPEATS, length) * 1e-3 for length in cls._LENGTHS[f]}
            print(f'{cls._FUNCS[f]} Done')

        cls.print_result()
        cls.render_graph(levenshtein_recurs, damerau_levenshtein_recurs)
        # cls.render_graph(levenshtein_recurs, levenshtein_recurs_mem)
        # cls.render_graph(damerau_levenshtein, damerau_levenshtein_recurs)
        cls.render_graph(damerau_levenshtein, levenshtein_recurs_mem)

    @classmethod
    def print_result(cls) -> None:
        for func, description in cls._FUNCS.items():
            print(f'{description}:')
            for length, result in cls._RESULTS[func].items():
                print(f'\t{length} символов: {round(result, 3)} µs')
            print()

    @classmethod
    def render_graph(cls, *args) -> None:
        plt.clf()

        plt.xlabel('Длина строки')
        plt.ylabel('Время, мс')
        plt.grid(axis='y', color='gray', linewidth=0.5)

        for func in args:
            x, y = [], []
            for length, result in cls._RESULTS[func].items():
                x.append(length)
                y.append(result)

            plt.plot(x, y, '-o', label=cls._FUNCS[func])
        plt.xticks(ticks=list(max(cls._LENGTHS[args[0]], cls._LENGTHS[args[1]])))  # TODO
        plt.legend()
        plt.savefig('measures.png')
        plt.show()

    @staticmethod
    def _test_function(func: LevenshteinFunc, repeat: int, length1: int, length2: Optional[int] = None) -> int:
        import functools
        import timeit
        if length2 is None:
            length2 = length1

        s1, s2 = Analyzer._generate_string(length1), Analyzer._generate_string(length2)
        # return timeit(stmt=lambda: func(s1, s2), timer=process_time_ns, number=1)
        return min(timeit.Timer(stmt=functools.partial(func, s1, s2), timer=process_time_ns).repeat(5, repeat)) / repeat

    @staticmethod
    def _generate_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    @staticmethod
    def mem_iterative() -> int:
        pass

    @staticmethod
    def mem_recursive() -> int:
        pass

    @staticmethod
    def mem_cached() -> int:
        pass
