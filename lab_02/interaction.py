import time
from typing import Optional

from lib import func_description, MatrixInt
from termcolor import colored, cprint


class UserInteraction:
    _M: int = 0
    _N: int = 0
    _Q: int = 0

    _TIME: Optional[float] = None

    def _read_dimensions(self) -> tuple[int, int, int]:
        ans = tuple(map(int, input().strip().split()))
        return ans[0], ans[1], ans[2]

    def start(self) -> None:
        cprint('Введите M, N, Q: ', color='yellow', attrs=['bold'], end='')

        try:
            self._M, self._N, self._Q = self._read_dimensions()
        except:
            cprint('Некорректный ввод!', color='red', attrs=['bold'])
            return

        if any([self._M <= 0, self._N <= 0, self._Q <= 0]):
            cprint('Некорректный ввод!', color='red', attrs=['bold'])
            return

        cprint('Сгенерировать матрицы автоматически?[Y/n]: ', color='yellow', attrs=['bold'], end='')
        lm, rm = self._get_matrices(input().strip().lower() != 'n')

        cprint("\nМатрица №1:", color='yellow', attrs=['bold'])
        cprint(lm, attrs=['bold'])
        cprint("\nМатрица №2:", color='yellow', attrs=['bold'])
        cprint(rm, attrs=['bold'])
        print()

        self.go(lm, rm)

    def _get_matrices(self, auto: bool) -> tuple[MatrixInt, MatrixInt]:
        if auto:
            lm, rm = MatrixInt(self._M, self._N).fill_rand(), MatrixInt(self._N, self._Q).fill_rand()
        else:
            lm, rm = self.input_matrix(self._M, self._N, '№1'), self.input_matrix(self._N, self._Q, '№2')

        return lm, rm

    @staticmethod
    def go(lm: MatrixInt, rm: MatrixInt) -> None:
        for func in func_description:
            start = time.process_time_ns()
            res = func(lm, rm)
            time_res = round((time.process_time_ns() - start) * 1e-6, 3)

            cprint(f'{func_description[func]} ', color='red', attrs=['bold'], end='')
            cprint(f'({time_res} ms):', color='blue', attrs=['bold'])
            cprint(f'{res}\n', color='green', attrs=['bold'])

    @staticmethod
    def input_matrix(m: int, n: int, name: str):
        matrix = MatrixInt(m, n)

        for line_number in range(m):
            cprint(f'Введите строку #{line_number} матрицы {name} ({m} x {n}): ', color='magenta', attrs=['bold'],
                   end='')
            try:
                res = list(map(int, input().strip().split()))
            except:
                cprint('Некорректный ввод!', color='red', attrs=['bold'])

                exit(-1)

            if len(res) != n:
                cprint('Некорректный ввод!', color='red', attrs=['bold'])

                exit(-1)

            for i in range(n):
                matrix[line_number][i] = res[i]

        print()
        return matrix
