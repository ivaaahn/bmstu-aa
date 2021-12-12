import sys
from copy import deepcopy

import consts
from matrix import MatrixType


# def calculate_routes(pos: int, paths_map: MatrixType, path: list[int], routes: list):
#     path = path.copy()
#
#     path.append(pos)
#
#     if len(path) < len(paths_map):
#         for src in range(len(paths_map)):
#             if src in path:
#                 routes.append(path)
#             else:
#                 calculate_routes(src, paths_map, path, routes)


def dist(paths_map: MatrixType, path: list[int]) -> int:
    return sum([paths_map[path[i]][path[(i + 1) % len(path)]] for i in range(len(path))])


def permutation_exist(path: list[int]) -> tuple[list[int], bool]:
    j = len(path) - 2
    while j != -1 and path[j] >= path[j + 1]:
        j -= 1

    if j == -1:
        return path, False

    k = len(path) - 1
    while path[j] >= path[k]:
        k -= 1

    path[j], path[k] = path[k], path[j]
    l, r = j + 1, len(path) - 1

    while l < r:
        path[l], path[r] = path[r], path[l]
        l, r = l + 1, r - 1

    return path, True


def brute_force(paths_map: MatrixType):
    path: list[int] = [_ for _ in range(len(paths_map))]
    shortest: list[int] = []

    curr_path = deepcopy(path)
    min_len = consts.MAX_INT

    state = True
    while state:
        if (curr_len := dist(paths_map, curr_path)) < min_len:
            min_len = curr_len
            shortest = deepcopy(curr_path)

        curr_path, state = permutation_exist(curr_path)

    return min_len, shortest

