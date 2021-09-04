from typing import Optional

from levenshtein import *


class UserInteraction:
    _MAP_ALG: dict[int, LevenshteinFunc] = {
        1: levenshtein_recursive,
        2: levenshtein_recursive_memo,
        3: damerau_levenshtein_default,
        4: damerau_levenshtein_recursive_memo,
    }

    _OUTPUT_MENU = '''
        Выберите алгоритм (введите число от 1 до 4):
        '1. Расстояние Левенштейна (Рекурсивный алгоритм)'
        '2. Расстояние Левенштейна (Рекурсивный алгоритм с мемоизацией)'
        '3. Расстояние Дамерау-Левенштейна (Итеративный алгоритм)'
        '4. Расстояние Дамерау-Левенштейна (Рекурсивный алгоритм с мемоизацией)'
        '''

    _INPUT_STRINGS_TEXT = '''
        Введите строку #{string_number}
    '''

    _OUTPUT_RESULT = '''
        Расстояние: {distance}
    '''

    _FUNC: Optional[LevenshteinFunc] = None

    def start(self) -> None:
        try:
            choice = int(input(self._OUTPUT_MENU))
            self._FUNC = self._MAP_ALG[choice]
        except KeyError:
            print('Некорректный дипазон')
            return
        except Exception:
            print('Некорректный ввод')
            return

        self.input_strings()

    def input_strings(self) -> None:
        str1 = input(self._INPUT_STRINGS_TEXT.format(string_number=1))
        str2 = input(self._INPUT_STRINGS_TEXT.format(string_number=2))
        distance = self._FUNC(str1, str2)
        print(self._OUTPUT_RESULT.format(distance=distance))
