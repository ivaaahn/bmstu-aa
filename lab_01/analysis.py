import string
import random
import matplotlib.pyplot as plt

from typing import Optional
from timeit import timeit
from time import process_time_ns

from levenshtein import LevenshteinFunc, func_description as levenshtein_func_description
from levenshtein import (
    levenshtein_recursive,
    levenshtein_recursive_memo,
    damerau_levenshtein_default,
    damerau_levenshtein_recursive_memo,
)


class Analyzer:
    _REPEATS = 10
    _FUNCS: dict[LevenshteinFunc, str] = levenshtein_func_description
    _RESULTS: dict[LevenshteinFunc, dict[int, int]] = dict()
    _LENGTHS: dict[LevenshteinFunc, list[int]] = {
        levenshtein_recursive: [0, 10],
        levenshtein_recursive_memo: [0, 10, 50, 100, 150, 200],
        damerau_levenshtein_default: [0, 10, 50, 100, 150, 200],
        damerau_levenshtein_recursive_memo: [0, 10, 50, 100, 150, 200],
    }

    @classmethod
    def start(cls) -> None:
        for f in cls._FUNCS:
            # print(f'{cls._FUNCS[f]} get started')
            cls._RESULTS[f] = {length: cls._test_function(f, cls._REPEATS, length) * 1e-6 for length in cls._LENGTHS[f]}
            # print(f'{cls._FUNCS[f]} Done')

        cls.print_result()
        cls.render_graph()

    @classmethod
    def print_result(cls) -> None:
        for func, description in cls._FUNCS.items():
            print(f'{description}:')
            for length, result in cls._RESULTS[func].items():
                print(f'\t{length} символов: {round(result, 3)} ms')
            print()

    @classmethod
    def render_graph(cls) -> None:
        plt.clf()

        plt.xlabel('Длина строки')
        plt.ylabel('Время, мс')
        plt.grid(axis='y', color='gray', linewidth=0.5)

        for func, description in cls._FUNCS.items():
            x, y = [], []
            for length, result in cls._RESULTS[func].items():
                x.append(length)
                y.append(result)

            plt.plot(x, y, '-o', label=cls._FUNCS[func])
        plt.xticks(ticks=list(cls._LENGTHS.values())[1])  # TODO
        plt.legend()
        plt.savefig('measures.png')
        plt.show()

    @staticmethod
    def _test_function(func: LevenshteinFunc, repeat: int, length1: int, length2: Optional[int] = None) -> int:
        if length2 is None:
            length2 = length1

        s1, s2 = Analyzer._generate_string(length1), Analyzer._generate_string(length2)
        return timeit(stmt=lambda: func(s1, s2), timer=process_time_ns, number=repeat)

    @staticmethod
    def _generate_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
