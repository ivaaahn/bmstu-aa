import random
import matplotlib.pyplot as plt
from time import process_time_ns
from lib import *


class Analyzer:
    _REPEATS = 10
    _RESULTS: dict[SortFuncType, dict[int, float]] = {func: {} for func in func_description}
    _SIZES: list[int] = [_ for _ in range(100, 1001, 100)]

    @classmethod
    def start(cls) -> None:
        for size in cls._SIZES:
            print(f'{size} get started')
            array = [random.randint(0, 99) for _ in range(size)]
            random.shuffle(array)
            for func, descr in func_description.items():
                print(f'\t{descr}: ', end='')
                cls._RESULTS[func][size] = cls._test_function(func, array, cls._REPEATS, size) * 1e-6
                print(f'Done')
            print(f'{size} Done')

        cls.print_result()
        cls.render_graph(bubble_sort, insertion_sort, selection_sort)

    @classmethod
    def print_result(cls) -> None:
        print(cls._RESULTS)

        for func, results in cls._RESULTS.items():
            print(f'{func_description[func]}:')
            for size, res_time in results.items():
                print(f'\t{size}: {round(res_time, 3)} ms')
            print()

    @classmethod
    def render_graph(cls, *args, **kwargs) -> None:
        plt.clf()

        plt.xlabel('Кол-во элементов')
        plt.ylabel('Время, ms')
        plt.grid(axis='y', color='gray', linewidth=0.5)

        for func in args:
            x, y = [], []
            for size, res_time in cls._RESULTS[func].items():
                x.append(size)
                y.append(res_time)

            plt.plot(x, y, '-o', label=func_description[func])

        plt.legend()
        plt.savefig('measures.png')
        plt.show()

    @staticmethod
    def _test_function(func: SortFuncType, array: ArrayInt, repeat: int, size: int) -> int:
        import functools
        import timeit

        return min(
            timeit.Timer(stmt=functools.partial(func, array, size), timer=process_time_ns).repeat(5, repeat)) / repeat
