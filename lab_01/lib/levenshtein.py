from .types import CacheMatrix


def levenshtein_recurs(s1: str, s2: str) -> tuple[int, int]:
    return _levenshtein_recurs(s1, s2, 0)


def _levenshtein_recurs(s1: str, s2: str, depth: int = 0) -> tuple[int, int]:
    if not (s1 and s2):
        return (len(s1) + len(s2)), depth

    if s1[-1] == s2[-1]:
        return _levenshtein_recurs(s1[:-1], s2[:-1], depth + 1)

    dist, depth = min(
        _levenshtein_recurs(s1[:-1], s2, depth + 1),
        _levenshtein_recurs(s1, s2[:-1], depth + 1),
        _levenshtein_recurs(s1[:-1], s2[:-1], depth + 1),
    )
    return dist + 1, depth


def levenshtein_recurs_mem(s1: str, s2: str, depth: int = 0) -> tuple[int, int, CacheMatrix]:
    _CACHE: CacheMatrix = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    result = _lev_rec_mem_inner(s1, s2, _CACHE, depth)
    return result[0], result[1], _CACHE


def _lev_rec_mem_inner(s1: str, s2: str, m: CacheMatrix, depth: int = 0) -> tuple[int, int]:
    ls1, ls2 = len(s1), len(s2)

    if m[ls1][ls2] is None:
        if not (s1 and s2):
            m[ls1][ls2] = ls1 + ls2
        elif s1[-1] == s2[-1]:
            m[ls1][ls2], depth = _lev_rec_mem_inner(s1[:-1], s2[:-1], m, depth + 1)
        else:
            dist, depth = min(_lev_rec_mem_inner(s1[:-1], s2, m, depth + 1),
                              _lev_rec_mem_inner(s1, s2[:-1], m, depth + 1),
                              _lev_rec_mem_inner(s1[:-1], s2[:-1], m, depth + 1))
            m[ls1][ls2] = dist + 1

    return m[ls1][ls2], depth
