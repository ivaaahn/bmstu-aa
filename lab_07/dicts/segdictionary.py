from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

from .dictionary import Dictionary, Pair


@dataclass
class SegPair:
    key: str
    value: Dictionary

    def print(self):
        print(f'{self.key}: ', end='')
        self.value.print()


class SegDictionary:
    def __init__(self, m: Dictionary):
        self._data: list[SegPair] = []

        self._parse_map(m)

    @property
    def data(self) -> list[SegPair]:
        return self._data

    def _parse_map(self, m: Dictionary):
        raw_dict = defaultdict(list)

        for pair in m.data:
            raw_dict[pair.key[0]].append(pair)

        self._parse_dict(raw_dict)

    def _parse_dict(self, raw_dict):
        self._data = [SegPair(k, Dictionary(lst=v)) for k, v in raw_dict.items()]

    def print(self):
        for item in self._data:
            item.print()

    def find(self, key: str) -> tuple[Optional[Pair], int]:
        k = key[0]

        count = 0
        for seg_pair in self._data:
            if seg_pair.key == k:
                res = seg_pair.value.find2(key)
                return res[0], count + res[1]

        return None, count
