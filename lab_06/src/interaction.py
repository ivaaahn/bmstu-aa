import time
from typing import Optional

from ants.matrix import MatrixType

from termcolor import colored, cprint
from ants.matrix import Matrix


class UserInteraction:
    _N: int = 0

    _TIME: Optional[float] = None

    @staticmethod
    def _read_dimensions() -> int:
        return int(input().strip())

    def _print_matr(self, m):
        for line in m:
            cprint(line, attrs=['bold'])

    def start(self) -> Optional[MatrixType]:
        cprint('Введите размерность матрицы (N): ', color='yellow', attrs=['bold'], end='')

        try:
            self._N = self._read_dimensions()
        except:
            cprint('Некорректный ввод!', color='red', attrs=['bold'])
            return

        if self._N <= 0:
            cprint('Некорректный ввод!', color='red', attrs=['bold'])
            return

        cprint('Сгенерировать матрицу автоматически?[Y/n]: ', color='yellow', attrs=['bold'], end='')
        m = self._get_matrices(input().strip().lower() != 'n')

        self._print_matr(m)
        print()

        return m

    def _get_matrices(self, auto: bool) -> MatrixType:
        return Matrix.generate(self._N) if auto else self.input_matrix(self._N)

    @staticmethod
    def input_matrix(n: int):

        m = Matrix.create(n, 0)

        for line_number in range(n):
            cprint(f'Введите строку #{line_number} матрицы ({n} x {n}): ', color='magenta', attrs=['bold'], end='')
            try:
                res = list(map(int, input().strip().split()))
            except:
                cprint('Некорректный ввод!', color='red', attrs=['bold'])
                exit(-1)

            if len(res) != n:
                cprint('Некорректный ввод!', color='red', attrs=['bold'])
                exit(-1)

            for i in range(n):
                m[line_number][i] = res[i]

        print()
        return m
