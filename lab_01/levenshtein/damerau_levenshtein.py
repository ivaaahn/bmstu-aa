from .types import CacheMatrix


def damerau_levenshtein_default(word_1: str, word_2: str) -> int:
    w1_len, w2_len = len(word_1), len(word_2)
    f = [[(i + j) if i * j == 0 else 0 for j in range(w2_len + 1)] for i in range(w1_len + 1)]

    for i in range(1, w1_len + 1):
        for j in range(1, w2_len + 1):
            if word_1[i - 1] == word_2[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            elif i >= 2 and j >= 2 and word_1[i - 1] == word_2[j - 2] and word_1[i - 2] == word_2[j - 1]:
                f[i][j] = 1 + min(
                    f[i - 1][j],
                    f[i][j - 1],
                    f[i - 1][j - 1],
                    f[i - 2][j - 2],
                )
            else:
                f[i][j] = 1 + min(
                    f[i - 1][j],
                    f[i][j - 1],
                    f[i - 1][j - 1],
                )

    return f[-1][-1]


def damerau_levenshtein_recursive_memo(word_1: str, word_2: str) -> int:
    _CACHE: CacheMatrix = [[None for _ in range(len(word_2) + 1)] for _ in range(len(word_1) + 1)]

    def _inner(w1: str, w2: str) -> int:
        w1_len, w2_len = len(w1), len(w2)

        if _CACHE[w1_len][w2_len] is None:
            if not (w1 and w2):
                _CACHE[w1_len][w2_len] = w1_len + w2_len
            elif w1[-1] == w2[-1]:
                _CACHE[w1_len][w2_len] = _inner(w1[:-1], w2[:-1])
            elif len(w1) >= 2 and len(w2) >= 2 and word_1[-1] == word_2[-2] and word_1[-2] == word_2[-1]:
                _CACHE[w1_len][w2_len] = 1 + min(
                    _inner(w1[:-1], w2),
                    _inner(w1, w2[:-1]),
                    _inner(w1[:-1], w2[:-1]),
                    _inner(w1[:-2], w2[:-2]),
                )
            else:
                _CACHE[w1_len][w2_len] = 1 + min(
                    _inner(w1[:-1], w2),
                    _inner(w1, w2[:-1]),
                    _inner(w1[:-1], w2[:-1]),
                )

        return _CACHE[w1_len][w2_len]

    return _inner(word_1, word_2)
