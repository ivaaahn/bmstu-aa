from random import sample
from typing import Union, Any

MatrixType = list[list[Any]]


class Matrix:
    @staticmethod
    def create(size: int, initial_value: Union[int, bool] = 0) -> MatrixType:
        return [[initial_value for _ in range(size)] for _ in range(size)]

    @staticmethod
    def read(nodes_count: int) -> MatrixType:
        return [list(map(int, input().split())) for _ in range(nodes_count)]

    @staticmethod
    def generate(nodes_count) -> MatrixType:
        return [sample(range(1, 1000), nodes_count) for _ in range(nodes_count)]
