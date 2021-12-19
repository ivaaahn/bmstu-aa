import string
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class Pair:
    key: str
    value: int


class Dictionary:
    def __init__(self, filename: Optional[str] = None, lst: Optional[list[Pair]] = None):
        self._data: list[Pair] = []

        if filename:
            self._parse_text(filename)
            print(len(self._data))
        else:
            self._data = lst

    def __len__(self) -> int:
        return len(self._data)

    @property
    def data(self):
        return self._data

    def _parse_dict(self, raw_dict: defaultdict):
        self._data = [Pair(k, v) for k, v in raw_dict.items()]

    def _sort(self):
        return sorted(self.data, key=lambda x: x.key)

    @staticmethod
    def _clear_word(word: str) -> str:
        word = word.translate(str.maketrans('', '', string.punctuation))
        return word.lower() if (word and word[0].isalpha()) else ""

    def _parse_text(self, filename: str):
        raw_dict = defaultdict(int)

        with open(filename, 'r') as text:
            for line in text:
                for word in line.split():
                    if word := self._clear_word(word):
                        raw_dict[word] += 1

        self._parse_dict(raw_dict)

    def print(self):
        for item in self._data:
            print(item)

    def find1(self, key: str) -> tuple[Optional[Pair], int]:
        count = 0
        for pair in self._data:
            count += 1
            if pair.key == key:
                return pair, count

        return None, count

    def find2(self, key: str) -> tuple[Optional[Pair], int]:
        count = 0
        a = self._sort()

        left, right = 0, len(a) - 1
        while right > left:
            mid = left + (right - left) // 2

            count += 1
            if key > a[mid].key:
                left = mid + 1
            elif key < a[mid].key:
                right = mid - 1
            else:
                return a[mid], count

        count += 1
        if a[right].key == key:
            return a[right], count

        return None, count
