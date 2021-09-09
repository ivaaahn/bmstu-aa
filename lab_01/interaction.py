import time
from pprint import pprint
from typing import Optional

from lib import (
    levenshtein_recurs,
    levenshtein_recurs_mem,
    damerau_levenshtein_recurs,
    damerau_levenshtein,
    LevenshteinFunc,
    CacheMatrix,
)

import lib
from timeit import timeit
from time import process_time_ns


# timeit.template = """
# def inner(_it, _timer{init}):
#     {setup}
#     _t0 = _timer()
#     for _i in _it:
#         retval = {stmt}
#     _t1 = _timer()
#     return _t1 - _t0, retval
# """

class UserInteraction:
    _MAP_ALG: dict[int, LevenshteinFunc] = {
        1: levenshtein_recurs,
        2: levenshtein_recurs_mem,
        3: damerau_levenshtein,
        4: damerau_levenshtein_recurs,
    }

    _OUTPUT_MENU = f'''
        Выберите алгоритм (введите число от 1 до 4):
        1. Расстояние {lib.func_description[_MAP_ALG[1]]}
        2. Расстояние {lib.func_description[_MAP_ALG[2]]}
        3. Расстояние {lib.func_description[_MAP_ALG[3]]}
        4. Расстояние {lib.func_description[_MAP_ALG[4]]}
        '''

    _INPUT_STRINGS_TEXT = '''
        Введите строку #{string_number}: 
    '''

    _OUTPUT_RESULT = '''
        Расстояние: {distance}\n
        Время выполнения {time} ms\n
        Матрица:\n{matrix}\n
        Максимальная глубина рекурсии: {depth}\n
        Количество используемой памяти: {memory} bytes\n
    '''

    _FUNC: Optional[LevenshteinFunc] = None

    _DIST: Optional[int] = None
    _M: Optional[str] = None
    _DEPTH: Optional[int] = None
    _MEM: Optional[int] = None
    _TIME: Optional[float] = None

    def start(self) -> None:
        try:
            choice = int(input(self._OUTPUT_MENU))
            self._FUNC = self._MAP_ALG[choice]
        except KeyError:
            print('Некорректный диапазон')
            return
        except Exception:
            print('Некорректный ввод')
            return

        self.input_strings()

    def input_strings(self) -> None:
        str1 = input(self._INPUT_STRINGS_TEXT.format(string_number=1))
        str2 = input(self._INPUT_STRINGS_TEXT.format(string_number=2))
        start = time.process_time_ns()
        data = self._FUNC(str1, str2)
        self._TIME = round((time.process_time_ns() - start) * 1e-6, 5)
        self.parse_data(data)
        print(self._OUTPUT_RESULT.format(distance=self._DIST, matrix=self._M, depth=self._DEPTH, memory=self._MEM,
                                         time=self._TIME))

    def parse_data(self, data: tuple) -> None:
        self._DIST = data[0]
        if isinstance(data[1], list):
            self._M = self.pretty_matrix(data[1])
            return

        self._DEPTH = data[1]

        if len(data) > 2:
            self._M = self.pretty_matrix(data[2])

    def pretty_matrix(self, m: CacheMatrix) -> str:
        s = [[str(e) for e in row] for row in m]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)