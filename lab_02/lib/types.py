import random
from typing import Optional, Callable

__all__ = ['VectorInt', 'MatrixInt', 'MulFuncType']

SourceMatrixInt = list[list[Optional[int]]]
SourceVectorInt = list[Optional[int]]


class VectorInt:
    def __init__(self, size: int) -> None:
        self._size = size
        self._src = self._init_vector()

    def _init_vector(self) -> SourceVectorInt:
        return [0 for _ in range(self._size)]

    @property
    def size(self) -> int:
        return self._size

    def __getitem__(self, item: int) -> int:
        return self._src[item]

    def __setitem__(self, item: int, value: int) -> None:
        self._src[item] = value

    def __str__(self) -> str:
        return ' '.join(map(str, self._src))

    def __repr__(self) -> str:
        return str(self)


class MatrixInt:
    def __init__(self, m: int, n: int) -> None:
        self._m = m
        self._n = n
        self._src = self._init_matrix()

    def _init_matrix(self) -> SourceMatrixInt:
        return [[0 for _ in range(self._n)] for _ in range(self._m)]

    def fill_rand(self) -> 'MatrixInt':
        for i in range(self._m):
            for j in range(self._n):
                self._src[i][j] = random.randint(0, 999)
        return self

    @property
    def m(self) -> int:
        return self._m

    @property
    def n(self) -> int:
        return self._n

    def __getitem__(self, item: int) -> list[Optional[int]]:
        return self._src[item]

    def __setitem__(self, item: int, value: int) -> list[Optional[int]]:
        return self._src[item]

    def __str__(self) -> str:
        s = [[str(e) for e in row] for row in self._src]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: 'MatrixInt') -> bool:
        for i in range(self._m):
            for j in range(self._n):
                if self._src[i][j] != other[i][j]:
                    return False
        return True


MulFuncType = Callable[[MatrixInt, MatrixInt], MatrixInt]
