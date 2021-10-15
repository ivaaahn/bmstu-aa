import random
import matplotlib.pyplot as plt
from time import process_time_ns
from lib import *
from lib.types import *

class Analyzer:
    _REPEATS = 50
    _RESULTS: dict[SortFuncType, dict[int, float]] = {func: {} for func in func_description}
    _SIZES: list[int] = [10, 50, 100, 250, 500, 750, 1000]
    @classmethod
    def start(cls) -> None:
        for size in cls._SIZES:
            print(f'{size} get started')
            array = [random.randint(0, 9999) for _ in range(size)]
            array.sort()
            array.reverse()
            for func, descr in func_description.items():
                curr_array = array.copy()
                print(f'\t{descr}: ', end='')
                cls._RESULTS[func][size] = cls._test_function(func, curr_array, cls._REPEATS) * 1e-6
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

        with open('saved/data.csv', 'w') as f:
            f.write(f'Size,BubbleSort,InsertSort,SelectSort\n')
            b, i, s = cls._RESULTS.values()
            for n, rb, ri, rs in zip(b.keys(), b.values(), i.values(), s.values()):
                f.write(f'{n},{round(rb, 4)},{round(ri, 4)},{round(rs, 4)}\n')

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
    def _test_function(func: SortFuncType, array: ArrayInt, repeats: int) -> int:
        import functools
        import timeit

        return timeit.timeit(stmt=lambda: func(array.copy(), len(array)), timer=process_time_ns, number=repeats) / repeats
