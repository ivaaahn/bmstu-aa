import matplotlib.pyplot as plt
from time import process_time_ns
from lib import MulFuncType, func_description, MatrixInt, simple_mul, win_mul, win_mul_imp


class Analyzer:
    _REPEATS = 5
    _FUNCS: dict[MulFuncType, str] = func_description
    _RESULTS: dict[MulFuncType, dict[int, dict[int, int]]] = {}
    _DIMS: dict[int, list[int]] = {0: [50 * x for x in range(1, 6)], 1: [50 * x + 1 for x in range(1, 6)]}

    @classmethod
    def start(cls) -> None:
        for f in cls._FUNCS:
            print(f'{cls._FUNCS[f]} get started')
            cls._RESULTS[f] = {}
            # cls._RESULTS[f][0] = {dim: cls._test_function(f, cls._REPEATS, dim) * 1e-9 for dim in cls._DIMS[0]}
            # print('Done 1/2')
            cls._RESULTS[f][1] = {dim: cls._test_function(f, cls._REPEATS, dim) * 1e-9 for dim in cls._DIMS[1]}
            print(f'{cls._FUNCS[f]} Done')

        cls.print_result()
        # cls.render_graph(simple_mul, win_mul, win_mul_imp, type_=0)
        cls.render_graph(simple_mul, win_mul, win_mul_imp, type_=1)
        # cls.render_graph(simple_mul, win_mul, win_mul_imp, type_=None)


    @classmethod
    def print_result(cls) -> None:
        for func, description in cls._FUNCS.items():
            print(f'{description}:')
            for t, result in cls._RESULTS[func].items():
                for dim, res_time in result.items():
                    print(f'\t{dim}x{dim}: {round(res_time, 3)} s')
                print()

    @classmethod
    def render_graph(cls, *args, **kwargs) -> None:
        plt.clf()

        plt.xlabel('Размерность')
        plt.ylabel('Время, с')
        plt.grid(axis='y', color='gray', linewidth=0.5)

        for func in args:
            x, y = [], []
            type_ = kwargs['type_']
            if type_ is None:
                for dim, res_time in sorted(tuple(cls._RESULTS[func][0].items()) + tuple(cls._RESULTS[func][1].items())):
                    x.append(dim)
                    y.append(res_time)

                plt.plot(x, y, '-o', label=cls._FUNCS[func])
            else:
                for dim, res_time in cls._RESULTS[func][kwargs['type_']].items():
                    x.append(dim)
                    y.append(res_time)

                plt.plot(x, y, '-o', label=cls._FUNCS[func] + f'({"нечет" if kwargs["type_"] else "чет"})')
        plt.legend()
        plt.savefig('measures2.png')
        plt.show()

    @staticmethod
    def _test_function(func: MulFuncType, repeat: int, dim: int) -> int:
        import functools
        import timeit

        lm, rm = MatrixInt(dim, dim).fill_rand(), MatrixInt(dim, dim).fill_rand()
        return min(timeit.Timer(stmt=functools.partial(func, lm, rm), timer=process_time_ns).repeat(1, repeat)) / repeat
