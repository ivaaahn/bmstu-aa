from cmath import inf

from .types import CacheMatrix


def damerau_levenshtein(s1: str, s2: str) -> tuple[int, CacheMatrix]:
    ls1, ls2 = len(s1), len(s2)
    m = [[(i + j) if i * j == 0 else 0 for j in range(ls2 + 1)] for i in range(ls1 + 1)]

    for i in range(1, ls1 + 1):
        for j in range(1, ls2 + 1):
            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1]
            else:
                m[i][j] = 1 + min(
                    m[i - 1][j],
                    m[i][j - 1],
                    m[i - 1][j - 1],
                    m[i - 2][j - 2]
                    if (i >= 2 and j >= 2) and all((s1[i - 1] == s2[j - 2], s1[i - 2] == s2[j - 1])) else inf
                )
    return m[-1][-1], m


def damerau_levenshtein_recurs(s1: str, s2: str, depth: int = 0) -> tuple[int, int]:
    if not (s1 and s2):
        return len(s1) + len(s2), depth

    if s1[-1] == s2[-1]:
        return damerau_levenshtein_recurs(s1[:-1], s2[:-1], depth + 1)

    ls1, ls2 = len(s1), len(s2)
    dist, depth = min(
        damerau_levenshtein_recurs(s1[:-1], s2, depth + 1),
        damerau_levenshtein_recurs(s1, s2[:-1], depth + 1),
        damerau_levenshtein_recurs(s1[:-1], s2[:-1], depth + 1),
        damerau_levenshtein_recurs(s1[:-2], s2[:-2], depth + 1)
        if (ls1 > 1 and ls2 > 1) and all((s1[-1] == s2[-2], s1[-2] == s2[-1])) else (inf, 0),
    )

    return dist + 1, depth

#
# def damerau_levenshtein_recursive_memo(word_1: str, word_2: str) -> int:
#     _CACHE: CacheMatrix = [[None for _ in range(len(word_2) + 1)] for _ in range(len(word_1) + 1)]
#
#     def _inner(w1: str, w2: str) -> int:
#         w1_len, w2_len = len(w1), len(w2)
#
#         if _CACHE[w1_len][w2_len] is None:
#             if not (w1 and w2):
#                 _CACHE[w1_len][w2_len] = w1_len + w2_len
#             elif w1[-1] == w2[-1]:
#                 _CACHE[w1_len][w2_len] = _inner(w1[:-1], w2[:-1])
#             elif len(w1) >= 2 and len(w2) >= 2 and word_1[-1] == word_2[-2] and word_1[-2] == word_2[-1]:
#                 _CACHE[w1_len][w2_len] = 1 + min(
#                     _inner(w1[:-1], w2),
#                     _inner(w1, w2[:-1]),
#                     _inner(w1[:-1], w2[:-1]),
#                     _inner(w1[:-2], w2[:-2]),
#                 )
#             else:
#                 _CACHE[w1_len][w2_len] = 1 + min(
#                     _inner(w1[:-1], w2),
#                     _inner(w1, w2[:-1]),
#                     _inner(w1[:-1], w2[:-1]),
#                 )
#
#         return _CACHE[w1_len][w2_len]
#
#     return _inner(word_1, word_2)
