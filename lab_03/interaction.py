import random
import time
from typing import Optional

from termcolor import cprint

from lib import func_description, ArrayInt


class UserInteraction:
    _N: int = 0
    _ARRAY: ArrayInt = []
    _TIME: Optional[float] = None

    def _read_array_size(self) -> None:
        self._N = int(input())

    def start(self) -> None:
        cprint('Введите длину массива (N): ', color='yellow', attrs=['bold'], end='')

        try:
            self._read_array_size()
        except:
            cprint('Некорректный ввод!', color='red', attrs=['bold'])
            return

        if self._N <= 0:
            cprint('Размер массива - положительное число', color='red', attrs=['bold'])
            return

        cprint('Сгенерировать массив автоматически (случайный элемент в диапазоне [0; 99]? [Y/n]: ', color='yellow',
               attrs=['bold'], end='')

        self._get_array(input().strip().lower() != 'n')

        cprint("\nМассив:", color='yellow', attrs=['bold'])
        cprint(self._ARRAY, attrs=['bold'])
        print()

        self.go()

    def _get_array(self, auto: bool) -> None:
        if auto:
            self.generate_array()
        else:
            self.input_array()

    def go(self) -> None:
        for func in func_description:
            start = time.process_time_ns()
            func(self._ARRAY, self._N)
            time_res = round((time.process_time_ns() - start) * 1e-3, 3)

            cprint(f'{func_description[func]} ', color='red', attrs=['bold'], end='')
            cprint(f'({time_res} μs):', color='blue', attrs=['bold'])
            cprint(f'{self._ARRAY}\n', color='green', attrs=['bold'])

    def input_array(self) -> None:
        cprint(f'Введите элементы массива в одну строку через пробел:', color='magenta', attrs=['bold'])

        res = []
        try:
            res = list(map(int, input().strip().split()))
        except:
            cprint('Некорректный ввод!', color='red', attrs=['bold'])
            exit(-1)

        if len(res) != self._N:
            cprint('Некорректный ввод!', color='red', attrs=['bold'])
            exit(-1)

        self._ARRAY = res.copy()
        print()

    def generate_array(self) -> None:
        self._ARRAY = [random.randint(0, 99) for _ in range(self._N)]
